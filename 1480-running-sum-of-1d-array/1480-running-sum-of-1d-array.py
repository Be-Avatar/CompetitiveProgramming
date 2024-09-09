class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        stk = []
        for i in range(len(nums)):
            stk.append(sum(nums[:i+1]))
        return stk