class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def gcd(a,b):
            while b:
                a, b = b, a%b
            return a
        def lcm(a,b):
            return (a*b) // gcd(a,b)
        l, r = 0, 1
        while r < len(nums):
            if gcd(nums[l], nums[r]) > 1:
                val = lcm(nums[l], nums[r])
                nums[l:r+1] = [val]
                if l > 0:
                    l -= 1
                r = l + 1
            else:
                l += 1
                r += 1
        return nums
