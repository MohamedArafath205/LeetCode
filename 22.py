class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(bracket, open, close):
            if len(bracket) == n*2:
                res.append(bracket)
                return
            if open < n:
                dfs(bracket+"(", open+1, close)
            if close < open:
                dfs(bracket+")", open, close+1)
        if n == 0:
            return []

        dfs("", 0, 0)

        return res
