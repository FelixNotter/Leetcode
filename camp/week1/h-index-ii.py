class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        l = 0
        r = len(citations)
        n = len(citations)
        def feasible(i):
            return n-i-1>=citations[i]
        while l < r:
            m = l+(r-l)//2
            if not feasible(m):
                r = m
            else:
                l = m+1
        return n-l

        