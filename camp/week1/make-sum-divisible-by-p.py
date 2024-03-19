class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        c = [0]
        total = sum(nums)
        if total%p == 0:
            return 0
        for i in range(len(nums)):
            c.append(c[-1]+nums[i])

        ans = len(nums)
        prev = {}
        for i in range(len(c)):
            prev[(c[i]%p)] = i
            if ((c[i]%p - total%p)%p) in prev:

                ans = min(ans,i - prev[((c[i]%p - total%p)%p)])
            
  
        return ans if ans < len(nums) else -1
