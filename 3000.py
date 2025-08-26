class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area = 0
        max_val = 0
        for i in dimensions:
            x, y = i
            area = x*y
            val = (x*x + y*y)**0.5
            if val > max_val or (val == max_val and area > max_area):
                max_area = area
                max_val = val
        return max_area
