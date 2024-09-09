class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runSum = []
        sum = 0
        for i in nums:
            sum+=i
            runSum.append(sum)

        return runSum