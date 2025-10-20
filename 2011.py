class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for val in operations:
            if val[1] == '+':
                res += 1
            else:
                res -= 1
        return res
