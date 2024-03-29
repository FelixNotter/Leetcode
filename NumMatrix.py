class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.prefix = [[0]*(COLS+1) for _ in range(ROWS+1)]
        
        for c in range(COLS):
            count = 0
            for r in range(ROWS):
                count+=matrix[r][c]
                self.prefix[r+1][c+1] += count
        for row in self.prefix:
            count = 0
            for i in range(len(row)):
                count+=row[i]  
                row[i] = count
                    
        
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return self.prefix[row2+1][col2+1] - self.prefix[row1][col2+1] - self.prefix[row2+1][col1]+ self.prefix[row1][col1]
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
