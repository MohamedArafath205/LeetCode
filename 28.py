class Solution(object):
    def strStr(self, haystack, needle):
        found = -1
        for i in range(len(haystack)):
            if needle == haystack[i:i+(len(needle))]:
                found = i
                break
        return found

# Runtime - 22ms
# Memory - 11.57MB
# Difficulty - Easy
