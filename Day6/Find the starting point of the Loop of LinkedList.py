# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        hm = defaultdict(int)
        if not head:
            return None
        while head.next:
            if hm[head] == head.next:
                return head
            hm[head] = head.next
            head = head.next

        return None
