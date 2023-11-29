class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        colors = [-1]*n
        adj = defaultdict(list)
        for src,dst in dislikes:
            adj[src].append(dst)
            adj[dst].append(src)
            
        def dfs(node,cur):
            if cur == -1:
                cur = 0
            if colors[node-1] != -1 and cur != colors[node-1]:
                return False
            if colors[node-1] != -1:
                return True
            colors[node-1] = cur
            cur = 1 if cur == 0 else 0
            for nei in adj[node]:
                if not dfs(nei,cur):
                    return False
            return True
            
            


        for i in range(1,n+1):
            if colors[i-1] != -1:
                continue
            if not dfs(i,colors[i-1]):
                return False
        return True
        