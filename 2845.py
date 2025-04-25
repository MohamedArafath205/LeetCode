class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefix = 0
        count_map = defaultdict(int)
        count_map[0] = 1
        result = 0

        for num in nums:
            if num % modulo == k:
                prefix += 1
            prefix %= modulo
            target = (prefix - k + modulo) % modulo
            result += count_map[target]
            count_map[prefix] += 1

        return result
