class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_nums = []
        new_nums.append(nums[0])
        for i in range(1, len(nums)):
            new_nums.append(sum(nums[:i+1]))
        return new_nums