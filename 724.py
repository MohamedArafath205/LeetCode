class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for mid in range(len(nums)):
            right_sum = total - left_sum - nums[mid]
            if right_sum == left_sum:
                return mid
            left_sum += nums[mid]
        return -1
