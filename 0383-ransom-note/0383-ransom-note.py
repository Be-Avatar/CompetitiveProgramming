class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran_dic = {}
        mag_dic = {}
        
        for i in ransomNote:
            if i in ran_dic:
                ran_dic[i] += 1
            else:
                ran_dic[i] = 1
                
        for j in magazine:
            if j in mag_dic:
                mag_dic[j] += 1
            else:
                mag_dic[j] = 1
                
        boolean = True
        for k in set(ransomNote):
            boolean = boolean and ran_dic[k] <= mag_dic.get(k, 0)
        return boolean