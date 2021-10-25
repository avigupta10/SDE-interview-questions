# Definition for singly-linked list.
from collections import defaultdict


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hm = defaultdict(int)
        if not head:
            return False
        while head.next:
            if hm[head] == head.next:
                return True
            hm[head] = head.next
            head = head.next
