class Solution:
    def numIslands(self, board: List[List[str]]) -> int:
        count = 0
        visited = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "1":
                    if (row, col) not in visited:
                        count += 1
                    self.dfs(board,row,col,visited)

        return count

    def dfs(self,board,row,col,visited):
        if self.notValid(board,row,col,visited):
            return

        visited.add((row,col))

        self.dfs(board,row+1,col,visited)#down
        self.dfs(board, row - 1, col, visited)#up
        self.dfs(board, row , col+1, visited)#right
        self.dfs(board, row, col - 1, visited)#left

    def notValid(self,board,row,col,visited):
        if row < 0 or col < 0 or row == len(board) or col == len(board[0]) or (row,col) in visited or board[row][col] == "0":
            return True
        return False