class Solution:
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res <<= 1
            res |= n&1
            n >>= 1
        return res

# Runtime - 10ms
# Memory - 11.36MB
# Difficulty - Easy
