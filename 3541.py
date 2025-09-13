class Solution:
    def maxFreqSum(self, s: str) -> int:
        c_map = defaultdict(int)
        for i in range(len(s)):
            c_map[s[i]] += 1
        vowels = ['a', 'e', 'i', 'o', 'u']
        cons = 0
        vow = 0
        for char, val in c_map.items():
            if char not in vowels:
                cons = max(cons, val)
            else:
                vow = max(vow, val)
        return cons+vow
