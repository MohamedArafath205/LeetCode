class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        arr1 = []
        final = []
        for num in nums1:
            if num not in nums2 and num not in arr1:
                arr1.append(num)
        final.append(arr1)
        arr2 = []
        for num in nums2:
            if num not in nums1 and num not in arr2:
                arr2.append(num)
        final.append(arr2)
        return final
