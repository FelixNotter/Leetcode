class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        window = set(nums)
        res= 0 
        for i in range(len(nums)):
            build = set()
            for j in range(i,len(nums)):
                build.add(nums[j])
                if build == window:
                    res+=1
        return res
