class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        stk = []
        for i in range(1, n+1):
            stk.append(str(i))
        if n >= 3:
            for j in range(2, n, 3):
                stk[j] = "Fizz"
        if n >= 5:
            for k in range(4, n, 5):
                stk[k] = "Buzz"
        if n >= 15:
            for l in range(14, n, 15):
                stk[l] = "FizzBuzz"
        return stk