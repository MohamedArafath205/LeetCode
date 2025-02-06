class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        max_ = max(len(nums1), len(nums2))
        arr = []
        for i in range(max_):
            if i < len(nums1):
                arr.append(nums1[i])
            if i < len(nums2):
                arr.append(nums2[i])
        arr.sort()
        mid = len(arr) // 2
        len_ = len(arr)
        print(len_)
        if len_ % 2 == 0:
            return (arr[mid] + arr[mid-1]) / 2 
        else:
            return arr[mid]
