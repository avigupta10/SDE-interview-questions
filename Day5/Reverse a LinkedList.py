class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        cur = head

        while cur is not None:
            nxt = cur.next
            cur.next, prev, cur = prev, cur, nxt
        return prev
