class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for val in asteroids:
            while stack and val < 0 and stack[-1] > 0:
                if stack[-1] + val < 0:
                    stack.pop()
                elif stack[-1] + val > 0:
                    val = 0
                else:
                    val = 0
                    stack.pop()
            if val:
                stack.append(val)
        return stack
