class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i = 9
        while i >= 0:
            c = 0 
            for j in range(len(num)):
                if str(i) == num[j]:
                    c += 1
                else:
                    c = 0
                
                if c == 3:
                    return  str(i)*3
            i -= 1
        return ""
