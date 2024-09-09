class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotateImage(mat):
            tao = [row.copy() for row in reversed(mat)]
            for i in range(len(mat)):
                for j in range(len(mat)):
                    mat[i][j] = tao[j][i]
        
        for k in range(4):
            rotateImage(mat)
            if mat == target:
                return True
        return False