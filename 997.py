class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = [0] * (n+1)
        trusted_by = [0] * (n+1)

        for u, v in trust:
            trusts[u] += 1
            trusted_by[v] += 1
        
        for person in range(1, n+1):
            if trusts[person] == 0 and trusted_by[person] == n-1:
                return person
        return -1
