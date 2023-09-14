class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(k):
            hours = 0
            for pile in piles:
                hours +=math.ceil(pile/k)
                if hours > h:
                    return False
            return True
        l = 1
        r = max(piles)
        while l < r:
            m = l+(r-l)//2
            if feasible(m):
                r = m
            else:
                l = m+1
        return l
        







        

        