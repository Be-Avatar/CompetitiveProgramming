class Solution:
    def isThree(self, n: int) -> bool:
        count = 2
        for i in range(2, (n//2) + 1):
            if n % i == 0:
                count += 1
        return count == 3                
        