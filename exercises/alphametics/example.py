from itertools import permutations, chain, product


def digPerms(digset, nzcharset, okzcharset):
    nzcnt = len(nzcharset)
    okzcnt = len(okzcharset)
    totcnt = nzcnt + okzcnt
    nzdigset = digset - set((0,))
    nzdigsetcnt = len(nzdigset)
    digsetcnt = len(digset)
    if totcnt < 1:
        return [()]
    elif digsetcnt < totcnt or nzdigsetcnt < nzcnt:
        return []
    elif nzcnt == 0 or digsetcnt == nzdigsetcnt:
        return permutations(digset, totcnt)
    elif okzcnt == 0:
        return permutations(nzdigset, totcnt)
    else:
        poslst = list(range(nzcnt, totcnt))
        return chain(permutations(nzdigset, totcnt),
                     map(lambda x: x[0][:x[1]] + (0,) + x[0][x[1]:],
                         product(permutations(nzdigset, totcnt - 1),
                                 poslst)))


def check_rec(eqparams, tracecombo=(dict(), 0, set(range(10))), p=0):
    maxp, tchars, unzchars, uokzchars = eqparams
    prevdict, cover, remdigs = tracecombo
    if p == maxp:
        if cover == 0:
            return prevdict
        else:
            return dict()
    diglets = tuple(unzchars[p]) + tuple(uokzchars[p])
    for newdigs in digPerms(remdigs, unzchars[p], uokzchars[p]):
        testdict = prevdict.copy()
        testdict.update(zip(diglets, newdigs))
        testsum = cover + sum([testdict[c] * v
                               for c, v in tchars[p].items()])
        d, r = divmod(testsum, 10)
        if r == 0:
            rectest = check_rec(eqparams,
                                (testdict, d, remdigs - set(newdigs)),
                                p + 1)
            if len(rectest) > 0:
                return rectest
    return dict()


def solve(an):
    fullexp = [list(map(lambda x: list(reversed(x.strip())), s.split("+")))
               for s in an.strip().upper().split("==")]
    maxp = max([len(w) for s in fullexp for w in s])
    nzchars = set([w[-1] for s in fullexp for w in s])

    unzchars = []
    uokzchars = []
    tchars = []
    for i in range(maxp):
        tchars.append(dict())
        unzchars.append(set())
        uokzchars.append(set())

    for si, s in enumerate(fullexp):
        sgn = 1 - (si << 1)
        for w in s:
            for p, c in enumerate(w):
                if c not in tchars[p]:
                    tchars[p][c] = 0
                tchars[p][c] += sgn

    totchars = set()
    for p, chardict in enumerate(tchars):
        for c, cnt in chardict.copy().items():
            if cnt == 0:
                del chardict[c]
            elif c not in totchars:
                if c in nzchars:
                    unzchars[p].add(c)
                else:
                    uokzchars[p].add(c)
                totchars.add(c)

    return check_rec((maxp, tchars, unzchars, uokzchars))
