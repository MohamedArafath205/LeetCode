class Solution(object):
    def countBits(self, n):
        arr = []
        for i in range(n+1):
            arr.append(bin(i).count('1'))
        return arr
# Runtime - 54ms
# Memory - 15.50MB
# Difficulty - Easy
