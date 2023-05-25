class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ROWS = len(mat)
        COLS = len(mat[0])
        isOdd = True if ROWS % 2 != 0 else False

        total = 0
        for r in range(ROWS):
            total += mat[r][r]
            total += mat[r][ROWS-r-1]
        if isOdd:
            total -= mat[ROWS//2][COLS//2]
        return total
