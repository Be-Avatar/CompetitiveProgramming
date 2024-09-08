class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}
        for i in range(len(heights)):
            dic[heights[i]] = names[i]
        sorted_heights = reversed(sorted(heights))
        
        ans = []
        for j in sorted_heights:
            ans.append(dic[j])
        return ans