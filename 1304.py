class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n%2 == 0:
            for i in range(-(n//2), (n//2)+1):
                if i != 0:
                    res.append(i)
        if n%2 == 1:
            for i in range(-(n//2), (n//2)+1):
                res.append(i)
        return res
