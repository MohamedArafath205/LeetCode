class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashmap = defaultdict(int)
        for i in range(1, n+1):
            digit_sum = sum(int(d) for d in str(i))
            hashmap[digit_sum] += 1
        max_count = max(hashmap.values())
        return sum(1 for count in hashmap.values() if count == max_count)
