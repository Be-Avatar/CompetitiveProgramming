class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = set(nums1)
        n2 = set(nums2)
        stk = []
        for i in n1:
            if i in n2:
                stk.append(i)
        return stk