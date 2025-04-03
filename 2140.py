class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @lru_cache(None)
        def backtrack(i):
            if i >= len(questions):
                return 0
            points, brainpower = questions[i]
            return max(backtrack(i+1), points + backtrack(i + 1 + brainpower))
        return backtrack(0)
