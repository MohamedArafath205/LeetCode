class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        top = Counter(tops)
        bottom = Counter(bottoms)
        max_val = max(max(top, key=top.get), max(bottom, key=bottom.get))
        swap = 0
        for i in range(len(tops)):
            if top[max_val] > bottom[max_val]:
                if tops[i] != max_val and bottoms[i] == max_val:
                    tops[i], bottoms[i] = bottoms[i], tops[i]
                    swap += 1
            else:
                if bottoms[i] != max_val and tops[i] == max_val:
                    tops[i], bottoms[i] = bottoms[i], tops[i]
                    swap +=1
        
        if len(Counter(tops)) == 1 or len(Counter(bottoms)) == 1:
            return swap
        else:
            return -1 
