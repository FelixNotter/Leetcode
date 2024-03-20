class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = (10**9)+7
        adj = defaultdict(list)
        for u,v,t in roads:
            adj[u].append((v,t))
            adj[v].append((u,t))
        queue = [(0,0)]
        heapify(queue)
        visit = set()
        res = [0]*n
        while queue:
            cost,node = heappop(queue)
            if node in visit:continue
            res[node] = cost
            visit.add(node)
            for nei,c in adj[node]:
                if nei in visit:continue
                heappush(queue,(c+cost,nei))
        memo = {}
        def dp(node,cost):
            if node in memo:return memo[node]
            if cost == res[-1]:
                return 1
            add = 0
            for nei,c in adj[node]:
                if res[nei]+c+cost<=res[-1]:
                    add+=dp(nei,c+cost)
            memo[node] = add 
            return memo[node]
        return dp(n-1,0) % 1000000007



