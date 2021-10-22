from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])
        for i in intervals:
            if not res or res[-1][1] < i[0]:
                print(i)
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        return res


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

print(Solution().merge(intervals))