class Node(object):
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        node = self.tail
        if node is None or node.prev is None:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return node.value

    def shift(self):
        node = self.head
        if node is None or node.next is None:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return node.value

    def unshift(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def __len__(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

        return
