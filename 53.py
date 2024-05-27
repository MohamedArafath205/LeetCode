class Solution(object):
    def maxSubArray(self, nums):
        max_arr = nums[0]
        cur_sum = 0
        for i in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += i
            max_arr = max(cur_sum, max_arr)
        return max_arr

# Runtime - 545ms
# Memory - 24.88 MB
# Difficulty - Medium
