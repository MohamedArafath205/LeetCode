class Solution(object):
    def mergeAlternately(self, word1, word2):
        word = []
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                word.append(word1[i])
            if i < len(word2):
                word.append(word2[i])
        return ''.join(word)

# Runtime - 18 ms
# Memory - 11.45 MB
# Difficulty - Medium
