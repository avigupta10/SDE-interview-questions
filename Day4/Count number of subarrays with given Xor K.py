from collections import defaultdict


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def solve(self, arr, m):
        HashTable = defaultdict(int)
        HashTable[0] = 1
        count = 0
        curSum = 0
        for i in arr:
            curSum ^= i
            if HashTable[curSum ^ m]:
                count += HashTable[curSum ^ m]
            HashTable[curSum] += 1
        return count
