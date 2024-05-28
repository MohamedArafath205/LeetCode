class Solution(object):
    def maxProduct(self, nums):
        max_sub = max(nums)
        min_prod, max_prod = 1, 1 
        for n in nums:
            if n == 0:
                min_prod, max_prod = 1, 1
            tmp = max_prod * n
            max_prod = max(n*max_prod, n*min_prod, n)
            min_prod = min(tmp, n*min_prod, n)
            max_sub = max(max_sub, max_prod)
        return max_sub

# Runtime - 49ms
# Memory - 11.90 MB
# Difficulty - Medium
