class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)//3
        i = len(piles) - 2
        total = 0
        while n > 0:
            total += piles[i]
            n-=1
            i-=2
        return total
