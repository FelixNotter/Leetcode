class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = -float('inf')
        l = 0
        window = 0
        for r in range(len(nums)):
            window += nums[r]
            if r - l + 1 > k:
                window -= nums[l]
                l+=1
            if r - l + 1 == k:
                res = max(res,window/k)
            
        return res
