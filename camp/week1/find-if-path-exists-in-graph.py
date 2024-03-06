class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parents = [i for i in range(n)]
        rank = [0]*n
        def find(n):
            if n == parents[n]:
                return n
            parents[n] = find(parents[n])
            return parents[n]
        def union(a,b):
            n1 = find(a)
            n2 = find(b)
            if n1 == n2:
                return 
            if rank[n1] < rank[n2]:
                parents[n1] = n2
            elif rank[n2] < rank[n1]:
                parents[n2] = n1
            else:
                parents[n2] = n1
                rank[n1] +=1
        for u,v in edges:
            union(u,v)
    
        return find(source) == find(destination)