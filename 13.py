class Solution(object):
    def romanToInt(self, s):
        sum_ = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i:i+2] == "IV":
                sum_ += 4
                i += 2
            elif i < len(s) - 1 and s[i:i+2] == "IX":
                sum_ += 9
                i += 2
            elif i < len(s) - 1 and s[i:i+2] == "XL":
                sum_ += 40
                i += 2
            elif i < len(s) - 1 and s[i:i+2] == "XC":
                sum_ += 90
                i += 2
            elif i < len(s) - 1 and s[i:i+2] == "CD":
                sum_ += 400
                i += 2
            elif i < len(s) - 1 and s[i:i+2] == "CM":
                sum_ += 900
                i += 2
            else:
                if s[i] == "I":
                    sum_ += 1
                elif s[i] == "V":
                    sum_ += 5
                elif s[i] == "X":
                    sum_ += 10
                elif s[i] == "L":
                    sum_ += 50
                elif s[i] == "C":
                    sum_ += 100
                elif s[i] == "D":
                    sum_ += 500
                elif s[i] == "M":
                    sum_ += 1000
                i += 1
        return sum_

# Runtime - 36ms
# Memory - 11.62MB
# Difficulty - Easy
