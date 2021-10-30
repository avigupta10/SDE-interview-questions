from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        pre, suff = [], []
        l1,l2 = height[0],height[-1]
        for i in height:
            if i > l1:
                l1 = i
            pre.append(l1)
        for i in height[::-1]:
            if i > l2:
                l2 = i
            suff.append(l2)
        suff.reverse()
        ans = 0
        for i in range(len(height)):
            ans += min(pre[i],suff[i]) - height[i]
        return ans


print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
