class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) < 5:
            return 0
        r = len(nums)-3-1
        ans = float("inf") 
        l = 0
        while r < len(nums):
            ans = min(ans,nums[r]-nums[l])
            l+=1
            r+=1
        return ans

        