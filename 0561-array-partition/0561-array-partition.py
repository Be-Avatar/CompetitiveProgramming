class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        k = 0
        for i in range(len(nums)//2):
            ans += nums[k]
            k += 2
        return ans