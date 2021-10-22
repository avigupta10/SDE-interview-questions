from typing import List


class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = 1
        s = set()
        ans = [0, 0]
        for i in A:
            if i in s:
                ans[0] = i
            else:
                s.add(i)
        while n < len(A) + 1:
            if n not in s:
                ans[1] = n
            n += 1
        return ans


print(Solution().repeatedNumber([3, 1, 2, 5, 3]))