"""
# Definition for a Node.
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        hm = {}
        cur = head
        while cur:
            hm[cur] = Node(cur.val, None, None)
            cur = cur.next
        temp = head
        while temp:
            if temp.next:
                hm[temp].next = hm[temp.next]
            if temp.random:
                hm[temp].random = hm[temp.random]
            temp = temp.next
        return hm[head]
