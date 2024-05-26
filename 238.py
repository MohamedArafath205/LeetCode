class Solution(object):
    def productExceptSelf(self, nums):
        arr = [1] * len(nums)

        left_product = 1
        for i in range(len(nums)):
            arr[i] = left_product
            left_product *= nums[i]
        
        right_product = 1 
        for i in range((len(nums))-1, -1, -1):
            arr[i] *= right_product
            right_product *= nums[i]
        
        return arr
# Runtime - 272ms
# Memory - 19.10MB
# Difficulty - Medium
