# User function Template for python3

class Solution:
    # Function to find the minimum number of platforms required at the
    # railway station such that no train waits.
    def minimumPlatform(self, n, arr, dep):
        # code here
        arr.sort()
        dep.sort()
        res, plat = 0, 0
        i, j = 0, 0

        while i < n and j < n:
            if arr[i] <= dep[j]:
                plat += 1
                i += 1
            elif arr[i] > dep[j]:
                plat -= 1
                j += 1
            res = max(res, plat)
        return res