class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for src,dst in edges:
            adj[dst].append(src)
        res = []
        ans = []
        seen = set()
        def dfs(node):
            if node in seen:
                return 
            seen.add(node)
            for nei in adj[node]:
                dfs(nei)
            res.append(node)
        for i in range(n):
            dfs(i)
            
            res = res[:-1]
            res.sort()
            ans.append(res)
            res = []
            seen = set()
        return ans
        

        