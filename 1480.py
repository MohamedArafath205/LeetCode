class Solution(object):
    def runningSum(self, nums):
        arr = []
        num_ = 0
        for i in range(len(nums)):
            num_ += nums[i]
            arr.append(num_)
        return arr

# Runtime - 15ms
# Memory - 11.87 MB
# Difficulty - Easy
