class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        res =  0
        cur = 0 
        for r in range(len(nums)):
            cur += nums[r]
            cur%=k
            res += count[cur]
            count[cur] += 1
        return res