class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        ans = ''
        for i in range(len(num) - 1, -1, -1):
            if num[i] != '0':
                index = i
                break
        return num[: index + 1]