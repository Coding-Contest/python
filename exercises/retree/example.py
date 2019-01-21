def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")
    if len(set(preorder)) != len(preorder) != len(set(inorder)):
        raise ValueError("traversals must contain unique items")
    if not preorder:
        return {}
    value = preorder.pop(0)
    index = inorder.index(value)
    left_inorder, right_inorder = inorder[:index], inorder[index+1:]
    left_preorder = [x for x in preorder if x in left_inorder]
    right_preorder = [x for x in preorder if x in right_inorder]
    left = treeFromTraversals(left_preorder, left_inorder)
    right = treeFromTraversals(right_preorder, right_inorder)
    return {"v": value, "l": left, "r": right}
