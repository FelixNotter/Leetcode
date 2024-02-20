class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(total):
            if total in memo:
                return memo[total]
            if total == amount:
                return 0
            if total > amount:
                return amount+1
            possible = amount+1
            for coin in coins:
                possible = min(possible,1+dp(total+coin))
            memo[total] = possible
            return possible
        ans = dp(0)
        return ans if ans != amount+1 else -1
            
        