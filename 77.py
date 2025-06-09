class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def comb(arr, I):
            if len(arr) == k:
                res.append(arr[:])
                return
            
            for i in range(I, n+1):
                arr.append(i)
                comb(arr, i+1)
                arr.pop()
            
        comb([],1)
        return res
