from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        dic = Counter(nums)
        ans = []
        for i in dic:
            if dic[i] > len(nums)/3:
                ans.append(i)
        return ans


