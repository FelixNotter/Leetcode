class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        

        ROWS = len(s1)
        COLS = len(s2)
        dp = [[0]*COLS for _ in range(ROWS)]
        def compute(i,j):
            if (0 <= i < ROWS) and (0 <= j < COLS):
                return dp[i][j]
            return 0
        for i in range(ROWS-1,-1,-1):
            for j in range(COLS-1,-1,-1):
                if s1[i] == s2[j]:
                    dp[i][j] = 1+compute(i+1,j+1)
                else:
                    dp[i][j] = max(compute(i,j+1),compute(i+1,j))
        return dp[0][0]
        