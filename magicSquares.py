class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        res = 0

        for r in range(len(grid)-2):
            for c in range(len(grid[0])-2):
                if self.check(grid,r,c):
                    res +=1
        return res
    

    
        
    def check(self,board,r,c):
        initial_sum = 15
        visit = set()
        contains = set(range(1,10))
        
        #Making sure the grid is valid before any checks
        for i in range(3):
            for j in range(3):
                if (board[i+r][j+c] in visit) or (board[i+r][j+c] not in contains):
                    return False
                visit.add(board[i+r][j+c])
       
        # checking rows
        for i in range(3):
            row_add = 0
            for j in range(3):
                row_add += board[i+r][j+c]
            if row_add != initial_sum:
                return False
        
        #checking columns
        for i in range(3):
            column_add = 0
            for j in range(3):
                column_add += board[j+r][i+c]
            if column_add != initial_sum:
                return False
        #checking primary diagonal
        prim_add = 0
        for i in range(3):
            prim_add += board[i+r][i+c]
        if prim_add != initial_sum:
            return False
    
        
        
        
        return True
