class Solution:
    def findGCD(self, nums: List[int]) -> int:
        m = min(nums)
        M = max(nums)
        common_divisors = []
        for i in range(1, m+1):
            if m % i == 0 and M % i == 0:
                common_divisors.append(i)
        return max(common_divisors)