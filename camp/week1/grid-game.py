class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        prefix1 = [0]*(N+1)
        prefix2 = [0]*(N+1)
        count1 = 0
        count2 = 0
        for i in range(N):
            count1 += grid[0][i]
            prefix1[i+1] = count1
            count2 += grid[1][i]
            prefix2[i+1] = count2
        res = float("inf")
        print(prefix1,prefix2)
        for i in range(N):
            top = prefix1[N] - prefix1[i+1]
            bottom = prefix2[i]
            print(top,bottom)
            best = max(top,bottom)
            res = min(res,best)
        return res


    


