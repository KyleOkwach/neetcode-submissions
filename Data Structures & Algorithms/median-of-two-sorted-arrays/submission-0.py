class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted(nums1 + nums2)
        l, r = 0, len(arr) - 1
        res, k = 0, (l + r) // 2

        if len(arr) % 2 == 0:
            res = (arr[k] + arr[k+1]) / 2
        else:
            res = arr[k]
        
        return res