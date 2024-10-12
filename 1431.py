class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        arr = []
        for i in range(len(candies)):
            if candies[i]+extraCandies >= max(candies):
                arr.append(True)
            else:
                arr.append(False)
        return arr

# Runtime - 17ms
# Memory - 11.63MB
# Difficulty - Medium
