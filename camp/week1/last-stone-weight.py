class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heappush(maxHeap,-stone)
        while len(maxHeap) > 1:
            first = -1*heappop(maxHeap)
            second = -1*heappop(maxHeap)
            diff = abs(first-second)
            if diff:
                heappush(maxHeap,-diff)
        return -1*maxHeap.pop() if maxHeap else 0

        