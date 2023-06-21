class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        t = 0
        b = len(matrix)-1
        #invert the top row vertically
        while t < b:
            for c in range(len(matrix[0])):
                matrix[t][c],matrix[b][c] = matrix[b][c],matrix[t][c]
            t+=1
            b-=1
        #Transpose the matrix
        for r in range(len(matrix)):
            for c in range(r,len(matrix[0])):
                matrix[r][c],matrix[c][r] = matrix[c][r],matrix[r][c]
