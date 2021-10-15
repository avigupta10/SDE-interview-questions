from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        if numRows == 1: return [[1]]

        res = []
        for i in range(numRows):
            row = [1]
            for j in range(1, i):
                row.append(res[i - 1][j - 1] + res[i - 1][j])
            if not i == 0:
                row.append(1)
            res.append(row)
        return res


n = 9

obj = Solution()
print(obj.generate(n))
