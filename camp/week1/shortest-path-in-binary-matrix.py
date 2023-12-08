class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque([(0,0)])
        visit = set()
        res = 1
        direct = [[1,-1],[1,0],[1,1],[0,-1],[0,1],[-1,-1],[-1,0],[-1,1]]
        def violate(r,c):
            if (r,c) in visit:
                return True
            visit.add((r,c))
            
            if not(0 <= r < len(grid)):
                return True
            if not(0 <= c < len(grid[0])):
                return True
            if grid[r][c] == 1:
                return True

            return False






        
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
        
                if violate(r,c):
                    continue
                print(r,c)
                
                print(res)
                if r == n-1 and c == n-1:
                    return res
                
                for dr,dc in direct:
                    queue.append((r+dr,c+dc))
            res+=1
                
        return -1
    

        