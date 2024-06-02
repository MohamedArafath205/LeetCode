class Solution(object):
    def climbStairs(self, n):
        one, two = 1,1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one
# Runtime - 13ms
# Memory - 11.56MB
# Difficulty - Easy
