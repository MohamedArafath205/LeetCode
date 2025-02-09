class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        good_pair = 0
        count_map = defaultdict(int)
        n = len(nums)
        total_pairs = n * (n - 1) // 2
        for i, num in enumerate(nums):
            key = num - i
            good_pair += count_map[key]
            count_map[key] += 1
        return total_pairs - good_pair
