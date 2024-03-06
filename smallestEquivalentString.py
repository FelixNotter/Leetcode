class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parents = {chr(ord("a")+i):chr(ord("a")+i) for i in range(26)}
    

        def find(n):
            while n!=parents[n]:
                n = parents[n]
            return n
        def union(a,b):
            n1 = find(a)
            n2 = find(b)
            if n1 == n2:
                return 
            if n1 > n2:
                parents[n1] = n2
            else:
                parents[n2] = n1
            return

        
        for i in range(len(s1)):
        
            union(s1[i],s2[i])
        ans = []
        for i in range(len(baseStr)):
            ans.append(find(baseStr[i]))
        return "".join(ans)


        
