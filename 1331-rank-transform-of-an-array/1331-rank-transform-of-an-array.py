class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dic = {}
        eachElement = set(arr)
        sortedSet = sorted(eachElement)
        for i in range(len(sortedSet)):
            dic[sortedSet[i]] = i
        
        answer = []
        for j in range(len(arr)):
            answer.append(dic[arr[j]] + 1)
        return answer