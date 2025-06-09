class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def make_comb(idx, comb, total):
            if total == target:
                res.append(comb[:])
                return
            
            if total > target:
                return
            
            prev = -1 
            for i in range(idx, len(candidates)):
                if candidates[i] == prev:
                    continue
                comb.append(candidates[i])
                make_comb(i+1, comb, total+candidates[i])
                comb.pop()
                prev = candidates[i]
            return res
        return make_comb(0,[],0)
