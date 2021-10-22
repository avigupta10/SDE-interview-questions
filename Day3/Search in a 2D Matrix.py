class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r = -1
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                r = i
                break
        if target in matrix[r]:
            return True
        return False
