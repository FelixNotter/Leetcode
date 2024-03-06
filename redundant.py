class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges))]
        rank = [0]*(len(edges))
        def find(n):
            while n != parents[n]:
                parents[n] = parents[parents[n]]
                n = parents[n]
            return n
        def union(a,b):
            n1 = find(a)
            n2 = find(b)
            if n1 == n2:
                return True
            if rank[n1] < rank[n2]:
                parents[n1] = n2
            elif rank[n2] < rank[n1]:
                parents[n2] = n1
            else:
                parents[n2] = n1
                rank[n1]+=1
            return False
        for u,v in edges:
            if union(u-1,v-1):
                return [u,v]
        return []  
