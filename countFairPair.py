class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
       
        def helper(boundary):
            l = 0
            r = len(nums)-1
            res = 0
            while l < r:
                if nums[l]+nums[r] > boundary:
                    r-=1
                else:
                    res+=r-l
                    l+=1
            return res
        nums.sort()
        return helper(upper)-helper(lower-1)
        
        
