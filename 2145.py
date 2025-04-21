class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        x = y = s = 0
        for dif in differences:
            s += dif
            x = min(x,s)
            y = max(y,s)
        min_st = lower - x
        max_st = upper - y
        return max(0, max_st - min_st + 1)
