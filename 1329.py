class Solution:
    def longestPrefix(self, s: str) -> str:
        LPS = [0]*len(s)
        l = 0
        i = 1
        while i < len(s):
            if s[i] == s[l]:
                l += 1
                LPS[i] = l
                i += 1
            else:
                if l == 0:
                    LPS[i] = 0
                    i += 1
                else:
                    l = LPS[l-1]
        start = LPS[-1]
        return s[:start]
