class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        setNums = set(nums)
        if len(setNums) < 3:
            return max(nums)
        else:
            leet = sorted(setNums)
            return leet[len(leet)-3]