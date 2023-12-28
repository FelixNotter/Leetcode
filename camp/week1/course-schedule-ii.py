class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        incoming = [0]*numCourses
        for src,dst in prerequisites:
            adj[src].append(dst)
        visit = set()
        path = set()
        res = []
        def dfs(node):
            if node in path:
                return True
            if node in visit:
                return 
            visit.add(node)
            path.add(node)
            for nei in adj[node]:
                if dfs(nei):
                    return []
            res.append(node)
            path.remove(node)
        for i in range(numCourses):
            if dfs(i):
                return []
        
        return res
            
