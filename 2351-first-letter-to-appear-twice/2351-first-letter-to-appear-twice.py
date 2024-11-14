class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dic = {}
        for i in s:
            if i in dic:
                return i
            else:
                dic[i] = 1