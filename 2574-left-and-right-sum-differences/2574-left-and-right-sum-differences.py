class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = []
        rightSum = []
        ans = []
        for i in range(len(nums)):
            leftSum.append(sum(nums[:i]))
            rightSum.append((sum(nums[i:])) - nums[i])
            ans.append(abs(rightSum[i] - leftSum[i]))
        return ans