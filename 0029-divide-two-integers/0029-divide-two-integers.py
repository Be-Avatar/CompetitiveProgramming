class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        x=float(dividend)/float(divisor)
        if x > 2147483647:
            return 2147483647
        
        return int(x)