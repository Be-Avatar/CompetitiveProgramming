class Solution:
    def minElement(self, nums: List[int]) -> int:
        stk = []
        for i in nums:
            sum = 0
            while i > 0:
                sum += (i % 10)
                i //= 10
            stk.append(sum)
        return min(stk)