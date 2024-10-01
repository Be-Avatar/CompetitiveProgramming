class Solution:
    def reverseWords(self, s: str) -> str:
        stk = []
        for i in s.split():
            stk.append(i[::-1])
        return (' '.join(stk))