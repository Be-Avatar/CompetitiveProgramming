class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        stk = []
        for i in grid:
            stk.append(sum(i))
        return stk.index(max(stk))