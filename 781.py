class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        s = 0
        for num, val in count.items():
            size = num + 1
            group = ceil(val/size)
            s += size * group
        return s 
