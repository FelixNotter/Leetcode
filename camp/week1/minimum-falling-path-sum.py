class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        def safemove(r,c):
            if 0 <= r < n and 0<=c < n:
                return matrix[r][c]
            return float("inf")
        for r in range(n-2,-1,-1):
            for c in range(n-1,-1,-1):
                leftdiag = safemove(r+1,c-1)
                rightdiag = safemove(r+1,c+1)
                down = safemove(r+1,c)
                matrix[r][c] += min(leftdiag,rightdiag,down)
        return min(matrix[0])


        