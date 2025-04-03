class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        max_diff = 0
        prefix_sum = nums[0]
        for k in range(1, len(nums)):
            res = max(res, max_diff * nums[k])
            max_diff = max(max_diff, prefix_sum - nums[k])
            prefix_sum = max(prefix_sum, nums[k])
        return res
