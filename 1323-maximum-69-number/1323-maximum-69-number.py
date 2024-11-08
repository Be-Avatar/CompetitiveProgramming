class Solution:
    def maximum69Number (self, num: int) -> int:
        k = list(str(num))
        for i in range(len(k)):
            if k[i] == '6':
                k[i] = '9'
                break
        return int(''.join(k))
                