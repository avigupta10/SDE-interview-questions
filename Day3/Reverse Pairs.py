from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i < j and nums[i] > 2 * nums[j]:
                    ans += 1

        return ans


print(Solution().reversePairs([2,4,3,5,1]))
