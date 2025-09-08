class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if i + (n-i) == n and '0' not in str(i) and '0' not in str(n-i):
                return [i, n-i]
