import numpy as np
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        arr = np.array(matrix)
        return arr.transpose()