class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        def dp(i,buy):
            if (i,buy) in memo:return memo[(i,buy)]
            if i == len(prices):
                return 0
            if buy:
                memo[(i,buy)] = max(-prices[i]+dp(i+1,not buy),dp(i+1,buy))
            else:
                memo[(i,buy)] = max(prices[i]-fee+dp(i+1,not buy),dp(i+1,buy))
            return memo[(i,buy)]
        return dp(0,True)
        