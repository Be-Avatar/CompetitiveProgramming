class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        stk = []
        s = set(nums)
        for i in range(1,len(nums)+1):
            if(i not in s):
                stk.append(i)
        return stk