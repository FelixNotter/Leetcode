class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False
        target = sum(nums)//2
        memo = {}
        def dp(i,target):
            if (i,target) in memo:return memo[(i,target)]
            if i==len(nums):
                return target == 0
            memo[(i,target)] = dp(i+1,target-nums[i]) or dp(i+1,target)
            return memo[(i,target)]
        return dp(0,sum(nums)//2)
            
        

        