class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for c,i in enumerate(nums):
            x = target - i
            if x in nums:
                if nums.index(x) != c:
                    return [c, nums.index(x)]