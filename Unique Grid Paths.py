class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(m)] for _ in range(n)]

        def rec(i, j, m, n, dp):
            if i == n - 1 and j == m - 1:
                return 1
            if i >= n or j >= m:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            else:
                dp[i][j] = rec(i + 1, j, m, n, dp) + rec(i, j + 1, m, n, dp)
                return dp[i][j]

        return rec(0, 0, m, n, dp)


'''
OR
'''


class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        m+n-1
            C
             m-1
        :param m:
        :param n:
        :return:
        """
        N = m+n-2
        R = m-1
        ans = 1

        for i in range(R+1):
            ans *= (N-R+i)/i
        return ans

