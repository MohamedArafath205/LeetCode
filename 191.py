class Solution(object):
    def hammingWeight(self, n):
        return bin(n).count('1')

# Runtime - 22ms
# Memory - 11.51MB
# Difficulty - Easy
