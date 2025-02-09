class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        cur = 0
        for i in range(k):
            if s[i] in vowels:
                cur += 1
        max_vow = cur
        for i in range(k, len(s)):
            if s[i] in vowels:
                cur += 1
            if s[i-k] in vowels:
                cur -= 1
            max_vow = max(max_vow, cur)
        
        return max_vow
