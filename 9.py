class Solution(object):
    def isPalindrome(self, x):
        x_ = str(x)
        return x_[::-1]==x_
# Runtime - 24ms
# Memory - 11.62 MB
# Difficulty - Easy
