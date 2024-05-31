class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        else:
            return i+1
# Runtime - 111ms
# Memory - 12.93MB
# Difficulty - Easy
