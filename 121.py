class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            if(prices[i]<min_price):
                min_price = prices[i]
            elif(prices[i]-min_price>profit):
                profit = prices[i]-min_price

        return profit

# Runtime - 740 ms 
# Memory - 20.88 MB
# Difficulty - Easy
