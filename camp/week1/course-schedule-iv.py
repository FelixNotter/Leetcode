class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dp = [[float("inf")]*numCourses for  _ in range(numCourses)]

        for u,v in prerequisites:
            dp[u][v] = 1
        for i in range(numCourses):
            dp[i][i] = 0
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j])
        
        ans = []
        for s,d in queries:
            if dp[s][d] == float("inf"):
                ans.append(False)
            else:
                ans.append(True)
        return ans

        