class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target:
                    if i!=j:
                        return[i,j]
                    
        