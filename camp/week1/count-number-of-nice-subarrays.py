class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        res = odd =  0
        for r in range(len(nums)):
            odd += 1 if nums[r]% 2 == 1 else 0
            res += count[odd-k]
            count[odd]+=1
        return res
