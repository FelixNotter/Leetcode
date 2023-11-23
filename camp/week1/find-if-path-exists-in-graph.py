class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        for src,dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        visit =set()
        if source == destination:
            return True
    
        
        def dfs(node):
            if node == destination:
                return True
            if node in visit:
                return 
            visit.add(node)

            for neighbour in adj[node]:
                if dfs(neighbour):
                    return True
            return False

 
        return dfs(source)
     