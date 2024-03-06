class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents = [i for i in range(len(isConnected))]
        rank = [0]*(len(isConnected))

        def find(n):
            if n == parents[n]:
                return n
            parents[n] = find(parents[n])
            return parents[n]
        
        def union(a,b):
            n1 = find(a)
            n2 = find(b)
            if n1 == n2:
                return 0
            if rank[n2] < rank[n1]:
                parents[n2] = n1
            elif rank[n1] < rank[n2]:
                parents[n1] = n2
            else:
                parents[n1] = n2
                rank[n2]+=1
            return 1
        count = 0
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]:
                    count+=union(i,j)
        return len(isConnected) - count
        
        