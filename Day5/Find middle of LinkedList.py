import math


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        s = []

        while head is not None:
            s.append(head)

            head = head.next

        j = len(s) / 2

        if len(s) % 2 != 0:

            ce = j

            return s[int(math.ceil(ce))]

        else:

            return s[j]