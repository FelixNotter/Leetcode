class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hmap = {}
        res = 0
        for i in range(len(nums)):
            if nums[i] in hmap:
                res += hmap[nums[i]]
                hmap[nums[i]] +=1
            else:
                hmap[nums[i]] = 1
        return res
