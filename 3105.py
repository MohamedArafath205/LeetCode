class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        a = [1] * n
        b = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                a[i] += a[i-1]
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                b[i] += b[i-1]
        return max(max(a), max(b))
