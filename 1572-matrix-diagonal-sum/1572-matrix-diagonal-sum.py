class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if j == i:
                    sum += mat[i][j]
                if i + j == len(mat) - 1:
                    sum += mat[i][j]
        if len(mat) % 2 != 0:
            return sum - mat[len(mat)//2][len(mat)//2]
        else:
            return sum