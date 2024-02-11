class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for i in range(len(graph)):
            adj[i].extend(graph[i])
        state = [0]*(len(graph))
        res = []
        def dfs(node):
            if state[node] == 1:
                return 1
            if state[node] == 2:
                return 
            state[node] = 1
            for nei in adj[node]:
                if dfs(nei) == 1:
                    return 1
            res.append(node)
            state[node] = 2
        for i in range(len(graph)):
            if state[i] == 0:
                if dfs(i) == 1:
                    continue
        res.sort()
        return res