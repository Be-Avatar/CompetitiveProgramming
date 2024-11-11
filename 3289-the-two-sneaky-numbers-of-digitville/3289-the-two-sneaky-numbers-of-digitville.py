class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        dic = {}
        stk = []
        for i in nums:
            if i in dic:
                dic[i] += 1
                stk.append(i)
            else:
                dic[i] = 1
        return stk