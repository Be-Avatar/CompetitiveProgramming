class Solution:
    def isFascinating(self, n: int) -> bool:
        m = str(n) + str(n*2) +str(n*3)
        s = set()
        stk = []
        for i in m:
            if i not in s:
                stk.append(i)
                s.add(i)
        return ''.join(stk) == m and '0' not in m