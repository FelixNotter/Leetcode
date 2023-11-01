class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(p,nums):
            if len(nums) == 0:
                new = [p]
                return new
            local=[]
            ch = [nums[0]]
            for i in range(len(p)+1):
                f = p[0:i]
                l = p[i:len(p)]
                local+=helper(f+ch+l,nums[1:])

            return local
        return helper([],nums)