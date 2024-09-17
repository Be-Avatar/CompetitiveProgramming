class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        sentence = s1.split() + s2.split()
        uncommon = []
        dic = {}
        for i in sentence:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        for j in dic:
            if dic[j] == 1:
                uncommon.append(j)
        return uncommon