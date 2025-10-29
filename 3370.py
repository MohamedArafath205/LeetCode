class Solution:
    def smallestNumber(self, n: int) -> int:
        binary = list(bin(n))
        for i in range(2, len(binary)):
            binary[i] = '1'
        return (int(''.join(binary),2))
