from typing import List


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, 0

        for i in nums:
            if i == 0:
                red += 1
            elif i == 1:
                white += 1
            elif i == 2:
                blue += 1
        nums[:red] = [0] * red
        nums[red:white + red] = [1] * white
        nums[white + red:] = [2] * blue
