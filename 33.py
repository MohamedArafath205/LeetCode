class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            
            # Left subarray
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            # Right subarray
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else: 
                    l = mid + 1 
        return -1
# Runtime - 29ms
# Memory - 11.94MB
# Difficulty - Medium
