class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for i in range(n):
            tmp = [grid[i+j][j] for j in range(n-i)]
            tmp.sort(reverse=True)
            for j in range(n-i):
                grid[i+j][j] = tmp[j]
        
        for i in range(1, n):
            tmp = [grid[j][j+i] for j in range(n-i)]
            tmp.sort()
            for j in range(n-i):
                grid[j][j+i] = tmp[j]
        
        return grid
