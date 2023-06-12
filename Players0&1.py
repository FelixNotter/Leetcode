class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        hmap = {}
        for w,l in matches:
            if l in hmap:
                hmap[l]+=1
            else:
                hmap[l] = 1
        winners = set()
        losers = set()
        for w,l in matches:
            if w not in hmap:
                winners.add(w)
            if hmap[l] == 1:
                losers.add(l)
        winners = list(winners)
        losers = list(losers)
        winners.sort()
        losers.sort()
        return [winners,losers]
    
