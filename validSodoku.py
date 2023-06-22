class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            for c in range(9):
                if (board[r][c] != '.'):
                    if not self.isValidSpot(board,r,c):
                        return False
        return True

      
    
    def isValidSpot(self,board,r,c):
        spot1 = (r // 3)*3
        spot2 = (c // 3) *3
        for i in range(3):
            for j in range(3):
                if (i+spot1 != r or j+spot2 != c) and (board[i+spot1][j+spot2] != '.'):
                    if board[r][c] == board[i+spot1][j+spot2]:
                        return False
        for i in range(9):
            if (i != c) and (board[r][i] == board[r][c]):
                return False

        for i in range(9):
            if (i != r) and (board[i][c] == board[r][c]):
                return False
        return True
                        
