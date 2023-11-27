class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visit = set()
        adj = defaultdict(list)
        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):
                if r!=c:
                    if isConnected[r][c]:
                        adj[r+1].append(c+1)
        def dfs(num):
            if num in visit:
                return 
            visit.add(num)
            for nei in adj[num]:
                dfs(nei)

        res = 0 
        for i in range(1,n+1):
            if i not in visit:
                res+=1
                dfs(i)
        return res
