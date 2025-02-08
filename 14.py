class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(i) for i in strs])
        i = 0
        while i < min_len:
            for j in strs:
                if j[i] != strs[0][i]:
                    return j[:i]
            i += 1
        return strs[0][:i]
