class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        total = 0
        res = 0
        for i in range(len(nums)):
            total+=nums[i]
            res+=count[total%k]
            count[total%k]+=1
        return res
            
        