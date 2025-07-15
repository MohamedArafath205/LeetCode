class Solution:
    def isValid(self, word: str) -> bool:
        res = True if len(word) > 2 and word.isalnum() else False
        if not res:
            return res
        c,v = False, False
        vowels = set("aeiouAEIOU")
        for i in word:
            if i in vowels:
                v = True
            if i not in vowels and not i.isdigit():
                c = True
            if c and v:
                return True
        return False
