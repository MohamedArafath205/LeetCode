class Solution(object):
    def maxArea(self, height):
        res = 0
        l, r = 0, len(height)-1
        while l<=r:
            area = (r-l) * min(height[l], height[r])
            if ( area > res):
                res = area
            elif (height[l] > height[r]):
                r -= 1
            else:
                l += 1
        return res
# Runtime - 514ms
# Memory - 22.05MB
# Difficulty - Medium
