class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm_set = set(permutations(nums))
        ans = []
        for i in perm_set:
            ans.append(i)
        return ans