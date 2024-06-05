class Solution(object):
    def isValid(self, s):
        stack = []
        paranthese = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in paranthese:
                if stack and stack[-1] == paranthese[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False

# Runtime - 16ms
# Memory - 11.65MB
# Difficulty - Easy
