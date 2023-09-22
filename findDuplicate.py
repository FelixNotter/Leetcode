class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def feasible(m):
            count = 0
            for num in nums:
                if num <= m:
                    count+=1
            return count
        max(nums)
        l = 1
        r = max(nums)
        while l < r:
            m = l+(r-l)//2
            if feasible(m) > m:
                r = m
            else:
                l = m+1
        return l
        
        
