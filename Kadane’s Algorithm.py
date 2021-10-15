from typing import List


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ele = nums[0]
        temp = nums[0]
        for i in nums[1:]:
            temp = max(i, temp + i)
            ele = max(ele, temp)
            print(ele, temp)
        return ele


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
