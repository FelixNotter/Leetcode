
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        rank = {chr(i+ord("a")):0 for i in range(26)}
        parent = {chr(i+ord("a")):chr(i+ord("a")) for i in range(26)}
        def find(n):
            while n!= parent[n]:
                parent[n] = parent[parent[n]]
                n = parent[n]
            return n
        def union(a,b):
            n1 = find(a)
            n2 = find(b)
            if n1 == n2:
                return False
            if rank[n1] < rank[n2]:
                parent[n1] = parent[n2]
            elif rank[n2] < rank[n1]:
                parent[n2] = parent[n1]
            else:
                parent[n2] = parent[n1]
                rank[n1]+=1
            return True
        for i in range(len(equations)):
            if equations[i][1:3] == "==":
                union(equations[i][0],equations[i][3])
        print(parent)
        for i in range(len(equations)):
            if equations[i][1:3] == "!=":
                if find(equations[i][0]) == find(equations[i][3]):
                    return False
        return True
        