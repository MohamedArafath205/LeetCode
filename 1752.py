class Solution:
    def check(self, nums: List[int]) -> bool:
        dup = nums.copy()
        nums.sort()
        for i in range(len(nums)):
            nums[:] = nums[-1:] + nums[:-1]
            if nums == dup:
                return True
        return False
