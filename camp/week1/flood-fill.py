class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS,COLS = len(image),len(image[0])
        start_pix = image[sr][sc]

        def dfs(r,c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or image[r][c] != start_pix or image[r][c] == color:
                return 
            image[r][c] = color
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
    
        dfs(sr,sc)
        return image