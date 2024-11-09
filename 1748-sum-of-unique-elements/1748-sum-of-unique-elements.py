class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        sum = 0
        for j in dic:
            if dic[j] == 1:
                sum += j
        return sum