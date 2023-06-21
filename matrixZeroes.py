class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visit = set()
        def makeZero(matrix,r,c):
            
            for i in range(c):
                if matrix[r][i]:
                    visit.add((r,i))
                    matrix[r][i] = 0
            for i in range(r):
                if matrix[i][c]:
                    visit.add((i,c))
                    matrix[i][c] = 0
            for i in range(c+1,len(matrix[0])):
                if matrix[r][i]:
                    visit.add((r,i))
                    matrix[r][i] = 0
            
            for i in range(r+1,len(matrix)):
                if matrix[i][c]:
                    visit.add((i,c))
                    matrix[i][c] = 0
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                if not matrix[r][c] and (r,c) not in visit:
                    makeZero(matrix,r,c)
    
