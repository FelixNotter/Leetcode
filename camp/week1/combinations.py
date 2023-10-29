class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(curr,i):
            
            if len(curr) == k:
                res.append(curr.copy())
                return
            if i == n+1:
                return
            
            candidate = i
            curr.append(candidate)
            backtrack(curr,i+1)
            curr.pop()
            backtrack(curr,i+1)
           
        backtrack([],1)
        return res
