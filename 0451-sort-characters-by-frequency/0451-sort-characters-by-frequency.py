class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        stk = []
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        sorted_dict = dict(reversed(sorted(dic.items(), key=lambda x: x[1])))
        ans = ''
        for j in sorted_dict:
            ans += (dic[j] * j)
        return ans
