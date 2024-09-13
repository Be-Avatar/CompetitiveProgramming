class Solution:
    def reverse(self, x: int) -> int:
        reversed_x = int(str(abs(x))[::-1])
        if x < 0:
            reversed_x = -reversed_x
        if -2**31 <= reversed_x <= 2**31 - 1:
            return reversed_x
        else:
            return 0