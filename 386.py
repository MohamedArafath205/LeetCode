class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        arr = []
        def dfs(num):
            if num > n:
                return
            arr.append(num)
            for i in range(10):
                temp = num * 10 + i
                if temp > n:
                    break
                dfs(temp)
        
        for i in range(1, 10):
            dfs(i)
        return arr
