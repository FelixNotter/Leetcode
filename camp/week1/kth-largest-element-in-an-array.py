class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heappush(minHeap,-num)
        for _ in range(k):
            kth = heappop(minHeap)
        return -kth
