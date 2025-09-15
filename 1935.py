class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        res = 0
        for word in words:
            if not(set(word) & set(brokenLetters)):
                res += 1
        return res
