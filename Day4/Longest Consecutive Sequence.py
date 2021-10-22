class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        st = set(nums)
        for i in nums:
            curr = i
            ans = 1
            if curr - 1 not in st:
                while curr + 1 in st:
                    ans += 1
                    curr += 1
                res = max(res, ans)
        return res
    