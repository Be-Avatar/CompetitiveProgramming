class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = []
        for i in set(nums1):
            if i not in nums2:
                ans1.append(i)
        ans2 = []
        for j in set(nums2):
            if j not in nums1:
                ans2.append(j)
        answer = []
        answer.append(ans1)
        answer.append(ans2)
        return answer