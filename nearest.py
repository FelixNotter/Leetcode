class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
      
        res = math.inf
        minSoFar = math.inf
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                dst = abs(points[i][0]-x)+abs(points[i][1]-y)
                if dst < minSoFar:
                    minSoFar = dst
                    res = i
        

        return res if res!=math.inf else -1
