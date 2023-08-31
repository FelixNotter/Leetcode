class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        res = cur = 0
        for r in range(len(nums)):
            cur += nums[r]
            res+=count[cur-k]
            count[cur] +=1
        return res
