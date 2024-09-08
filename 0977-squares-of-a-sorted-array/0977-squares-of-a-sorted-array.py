class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = len(nums)
        i = 0
        while l != 0:
            nums[i] = nums[i] * nums[i]
            i += 1
            l -= 1
        return sorted(nums)