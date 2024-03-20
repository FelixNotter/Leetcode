class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        dp = [1]*n
        dp[0] = dp[1] = 0
        res = 0
        for i in range(2,n):
            if dp[i]:
                res+=1
                for j in range(i+i,n,i):
                    dp[j] = 0
        return res
