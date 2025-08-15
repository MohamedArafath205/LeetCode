class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return True if (n & (n-1)) == 0 else False 
