class Solution(object):
    def maximumWealth(self, accounts):
        f_sum = arr_sum = 0
        for arr in accounts:
            arr_sum = 0
            for i in range(len(arr)):
                arr_sum += arr[i]
            if arr_sum > f_sum:
                f_sum = arr_sum
        return f_sum

# Runtime - 29ms
# Memory - 11.39 MB
# Difficulty - Easy
