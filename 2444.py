class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        leftBound = mini = maxi = -1
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                leftBound = i
            if num == minK:
                mini = i
            if num == maxK:
                maxi = i
            count += max(0, min(mini, maxi) - leftBound)
        return count
