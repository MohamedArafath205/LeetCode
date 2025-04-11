class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = []
        for i in range(low, high+1):
            digit = str(i)
            half = len(digit) // 2
            if (sum(int(num) for num in digit[:half])) == (sum(int(num) for num in digit[-half:])) and len(digit) % 2==0:
                res.append(i)
        return len(res)
