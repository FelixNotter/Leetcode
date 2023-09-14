class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity):
            d = 1
            total = 0
            for weight in weights:
                total+=weight
                if total > capacity:
                    total = weight
                    d+=1
                    if weight > capacity or d > days:
                        return False
            return True
        l = min(weights)
        r = sum(weights) 
        ans = -1 
        while l <= r:
            m = l+(r-l)//2
            if feasible(m):
                ans = m
                r = m - 1
            else:
                l = m+1
        
        return ans
        