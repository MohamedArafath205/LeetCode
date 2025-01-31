class Solution:
    def reverseVowels(self, s: str) -> str:
        start = 0
        end = len(s)-1
        vow = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
        s = list(s)
        while start < end:
            if s[start] in vow:
                if s[end] in vow:
                    s[start], s[end] = s[end], s[start]
                    start += 1
                    end -= 1
                else:
                    end -= 1
            else:
                start += 1
        return "".join(s)
