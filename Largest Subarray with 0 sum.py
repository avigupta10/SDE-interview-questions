class Solution:
    def maxLen(self, n, arr):
        hm = {}
        s = 0
        ans = 0
        for i in range(n):
            s += arr[i]
            if s == 0:
                ans = i + 1
            else:
                if s not in hm:
                    hm[s] = i
                else:
                    ans = max(ans, i - hm[s])
        return ans
