class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        count = 0
        pos = 0
        mis = []
        while(pos < len(s1)):
            if s1[pos] != s2[pos]:
                count += 1
                mis.append(s1[pos])
                mis.append(s2[pos])
            if count > 2: 
                return False
            pos += 1
        if len(mis) == 4:
            if mis[0] == mis[3] and mis[1] == mis[2]:
                return True
        return False
