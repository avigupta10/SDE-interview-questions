from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        res = 0
        for i in nums:
            if i == 1:
                ans+=1
                res = max(res,ans)
            else:
                ans = 0
        return res