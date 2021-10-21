# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        c = 0
        main = head
        while head:
            c += 1
            head = head.next

        idx = c - n

        head = main

        if idx == 0:
            return main.next

        for _ in range(idx - 1):
            main = main.next

        if not head:
            return None
        if main.next is None:
            return None
        elif main.next.next:
            main.next = main.next.next
        else:
            main.next = None

        return head
