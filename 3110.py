class Solution:
    def scoreOfString(self, s: str) -> int:
        val = 0
        for i in range(len(s)-1):
            val += abs(ord(s[i]) - ord(s[i+1]))
        return val

# Runtime - 0ms
# Memory - 17.58MB
