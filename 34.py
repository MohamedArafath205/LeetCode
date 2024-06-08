class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        def leftIndex(nums, target):
            l, r = 0, len(nums)-1
            while l<=r:
                mid = (l+r)//2
                if nums[mid]<target:
                    l = mid+1
                else:
                    r = mid-1
            return l

        def rightIndex(nums, target):
            l, r = 0, len(nums)-1
            while l<=r:
                mid = (l+r)//2
                if nums[mid]<=target:
                    l = mid+1
                else:
                    r = mid-1
            return r

        left, right = leftIndex(nums, target), rightIndex(nums, target)
        if left <= right and left<len(nums) and nums[left] == target and nums[right] == target:
            return left, right
        else:
            return [-1, -1]

# Runtime - 63ms
# Memory - 12.70MB
# Difficulty - Medium
