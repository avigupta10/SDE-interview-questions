# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        123 312 231 123 312 231 123 312 231 123
        """

        def l(h):
            c = 0
            while h:
                c += 1
                h = h.next
            return c

        if not head:
            return None
        h = l(head)
        if k == 0 or (k % h) == 0:
            return head
        main = head

        for _ in range(h - (k % h) - 1):
            head = head.next

        tmp = head.next
        head.next = None
        print(tmp)
        c = tmp
        while tmp and tmp.next:
            tmp = tmp.next
        tmp.next = main
        return c
