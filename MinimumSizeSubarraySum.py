class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        ans = math.inf
        add = 0
        for r in range(len(nums)):
            add += nums[r]
            while add >= target:
                ans = min(ans,r-l+1)
                add-= nums[l]
                l+=1
        return ans if ans != math.inf else 0
