# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def leng(self, current):
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def reverse(self, head):
        if not head:
            return None
        prev = None
        cur = head
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        vals = []
        dummy = cur = ListNode(0)
        for i in lists:
            while i is not None:
                vals.append(i.val)
                i = i.next
        for j in vals:
            cur.next = ListNode(j)
            cur = cur.next
        return dummy.next

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        def rec(head, k):
            if self.leng(head) < k:
                res.append(head)
                return
            dummy = cur = head

            for _ in range(k - 1):
                cur = cur.next

            main = cur.next  # next
            cur.next = None
            ans = p = self.reverse(dummy)
            res.append(p)
            rec(main, k)

        res = []
        if k == 1:
            return head
        rec(head, k)
        return self.mergeKLists(res)
