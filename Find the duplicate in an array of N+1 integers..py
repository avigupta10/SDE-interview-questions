from typing import List


class Solution(object):
    def findDuplicate(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in A:
            i = abs(i)
            if A[i] < 0:
                return i
            A[i] = -A[i]
        return -1


nums = [1,3,4,2,2]
print(Solution().findDuplicate(nums))