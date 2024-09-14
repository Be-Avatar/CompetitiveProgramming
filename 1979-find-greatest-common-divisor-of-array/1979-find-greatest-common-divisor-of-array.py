class Solution:
    def findGCD(self, nums: List[int]) -> int:
        m = min(nums)
        M = max(nums)
        return gcd(m, M)