class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = {0:0,1:1}
        def dp(i):
            if i in memo:return memo[i]
            if i <= 0:
                return 0
            if i == 1:
                return 1
            if i%2 == 0:
                memo[i] = dp(i//2)
            else:
                t = (i-1)//2
                memo[i] = dp(t)+dp(t+1)
            return memo[i]
        ans = float("-inf")
        for i in range(n+1):
            ans = max(ans,dp(i))
        return ans
        
        