class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        res = []
        for val, num in c.items():
            if num > 1:
                res.append(val)
        
        return res 
