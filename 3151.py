class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        ans = True
        for i in range(len(nums)):
            if i+1 < len(nums):
                if nums[i] % 2 == 0:
                    if nums[i+1] % 2 != 1:
                        ans = False
                if nums[i] % 2 == 1:
                    if nums[i+1] % 2 != 0:
                        ans = False
        return ans
