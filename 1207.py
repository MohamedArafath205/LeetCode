class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        val = dict()
        for ch in arr:
            if ch not in val:
                val[ch] = arr.count(ch)
        if len(set(val.values())) == len(val):
            return True
        return False
