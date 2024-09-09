class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        setNums = set(nums)
        if len(setNums) < 3:
            return max(nums)
        else:
            setNums.remove(max(setNums))
            setNums.remove(max(setNums))
            return max(setNums)