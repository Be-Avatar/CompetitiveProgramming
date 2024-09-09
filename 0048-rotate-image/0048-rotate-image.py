class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        tao = [row.copy() for row in reversed(matrix)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = tao[j][i]