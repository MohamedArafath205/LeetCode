class Solution(object):
    def numberOfSteps(self, num):
        step = 0
        while num > 0:
            if (num%2==1):
                num -= 1
            else:
                num = num / 2
            step += 1
        return step

# Runtime - 14ms
# Memory - 11.55 MB
# Difficulty - Easy
