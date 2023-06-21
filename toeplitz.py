class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        c = 1
        r = ROWS - 1
        ans = True
        while r >= 0:
            ans = ans and self.check_diagonal(matrix,r,0)
            r -=1
     
        while c < COLS:
            print(matrix[0][c])
            ans = ans and self.check_diagonal(matrix,0,c)
            c +=1
        return ans
    
    def check_diagonal(self,matrix,r,c):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        while c >= 0 and c < COLS and r >= 0 and r < ROWS:
            if r+1 < ROWS and c+1 < COLS: 
                if matrix[r][c] != matrix[r+1][c+1]:
                    return False
            r += 1
            c += 1
        return True
