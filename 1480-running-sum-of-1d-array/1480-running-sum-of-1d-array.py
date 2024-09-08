class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_nums = []
        all_sum = sum(nums)
        for i in range(len(nums)):
            new_nums.append(all_sum - sum(nums[i+1:]))
        return new_nums