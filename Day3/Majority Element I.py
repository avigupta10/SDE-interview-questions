class Solution(object):
    def majorityElement(self, nums):
        majority_num = 0
        count = 0
        for num in nums:
            if count == 0:
                majority_num = num
            if majority_num != num:
                count -= 1
            else:
                count += 1
        return majority_num


'''
[2,2,1,1,1,2,2]
''' 