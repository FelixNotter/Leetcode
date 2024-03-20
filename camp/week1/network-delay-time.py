class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dp = [[float("inf")]*n for _ in range(n)]

        for u,v,w in times:
            dp[u-1][v-1] = w
        for i in range(n):
            dp[i][i] = 0
    
        for p in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j],dp[i][p]+dp[p][j])

        for num in dp[k-1]:
            if num == float("inf"):
                return -1
        return max(dp[k-1])
        
        

        