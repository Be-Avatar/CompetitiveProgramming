class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = nums1 + nums2
        total.sort()
        if len(total) % 2 == 1:
            return total[len(total)//2] / (1/1)
        else:
            return (total[len(total)//2] + total[len(total)//2 - 1]) / (2/1)