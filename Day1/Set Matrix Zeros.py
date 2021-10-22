from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def z_col(arr, col):
            for i in range(len(arr)):
                arr[i][col] = 0

        def z_row(arr, row):
            for i in range(len(arr)):
                arr[row][i] = 0

        ranges = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    ranges.append([i, j])
        for r, c in ranges:
            z_col(matrix, c)
            z_row(matrix, r)


mat = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]

obj = Solution()
obj.setZeroes(mat)
print(mat)
