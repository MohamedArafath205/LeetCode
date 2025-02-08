class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        mydict = defaultdict(int)
        count = 0 
        for num in nums:
            if mydict[k-num] > 0:
                count += 1
                mydict[k-num] -= 1
            else:
                mydict[num] += 1
        return count
