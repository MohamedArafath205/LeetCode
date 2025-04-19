from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        pair = 0
        nums.sort()
        for i in range(len(nums)):
            low = lower - nums[i]
            high = upper - nums[i]
            left = bisect_left(nums, low, i+1)
            right = bisect_right(nums, high, i+1)
            pair += (right - left)
        return pair
