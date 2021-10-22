from typing import List


class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(mat)):
            for j in range(i):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        n = len(mat)
        for i in range(n):
            for j in range(n // 2):
                mat[i][j], mat[i][-j - 1] = mat[i][-j - 1], mat[i][j]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
obj = Solution()
obj.rotate(matrix)
print(matrix)
