# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        output = ans
        carry = 0
        while l1 or l2 or carry:
            num1 = (l1.val if l1 else 0)
            num2 = (l2.val if l2 else 0)

            carry, value = divmod(num1 + num2 + carry, 10)

            output.next = ListNode(value)
            output = output.next

            if l1:
                l1 = l1.next
            else:
                return None

            if l2:
                l2 = l2.next
            else:
                None

        return ans.next