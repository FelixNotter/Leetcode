class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:



        visit = set()
        def dfs(r,c):
            if not(0 <= r < len(grid)) or not(0<=c < len(grid[0])) or (r,c) in visit or not grid[r][c]:
                return 0
            visit.add((r,c))
            return 1+(
                dfs(r+1,c)+
                dfs(r,c+1)+
                dfs(r-1,c)+
                dfs(r,c-1)
            )
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                res = max(res,dfs(r,c))
        return res
        