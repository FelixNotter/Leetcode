class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        def backtrack(curr,seen):
            if len(curr) == n:
                res.append(curr.copy())
                return
            if len(res) == k:
                return 
            for num in range(1,n+1):
                if num in seen:continue
                seen.add(num)
                curr.append(num)
                backtrack(curr,seen)
                seen.remove(num)
                curr.pop()
        backtrack([],set())
        
        return "".join(map(str,res[-1]))

        
        
        