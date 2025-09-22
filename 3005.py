class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        max_ = max(c.values())
        res = 0
        for val in c:
            if c[val] == max_:
                res += max_
        return res
