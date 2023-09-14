class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = len(nums)-1
        while l <= r:
            m = l+(r-l)//2
            left = float("-inf") if m-1 == -1 else nums[m-1] 
            right = float("-inf") if m+1 == n else nums[m+1]
            maxi = max(left,right)
            if nums[m] > maxi:
                return m
            if nums[m] < right:
                l = m+1
            else:
                r = m-1

