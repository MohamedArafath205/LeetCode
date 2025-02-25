class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort()
        
        count = 0
        x = None
        y = None
        
        for (ax, ay), (bx, by) in zip(stockPrices, stockPrices[1:]):
            dx = bx - ax
            dy = by - ay
            
            if x is None or x * dx != y * dy:
                count += 1
            
            x = dy
            y = dx
        
        return count
