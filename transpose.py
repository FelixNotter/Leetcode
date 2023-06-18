class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        ans = [[0]*ROWS for _ in range(COLS)]
        for c in range(COLS):
            for r in range(ROWS):
                ans[c][r] = matrix[r][c]
        return ans
