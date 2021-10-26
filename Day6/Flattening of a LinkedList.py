class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None


def merge(l1, l2):
    res = temp = Node(0)

    while l1 and l2:
        if l1.data < l2.data:
            temp.bottom = l1
            temp = temp.bottom
            l1 = l1.bottom
        else:
            temp.bottom = l2
            temp = temp.bottom
            l2 = l2.bottom
    temp.bottom = l1 or l2

    return res.bottom


def flatten(root):
    # Your code here
    if not root or not root.next:
        return root

    root.next = flatten(root.next)

    root = merge(root, root.next)
    return root