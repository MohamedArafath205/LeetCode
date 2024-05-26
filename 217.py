class Solution(object):
    def containsDuplicate(self, nums):
        list_ = len(nums)
        set_ = len(set(nums))
        if (list_>set_):
            return True
        else:
            return

# Runtime - 515ms
# Memory - 27.44 MB
