from sortedcontainers import SortedList
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        count = Counter([num % value for num in nums])
        i = 0
        while True:
            if count[i % value] > 0:
                count[i % value] -= 1
            else:
                return i
            i += 1
