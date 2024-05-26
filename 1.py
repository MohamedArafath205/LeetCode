class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(j==i):
                    j+=1
                else:    
                    if (nums[i]+nums[j]==target):
                        return i,j

# Memory - 12.31 MB
# RunTime - 5301 ms
# Difficulty - Easy
