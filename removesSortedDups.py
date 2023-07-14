class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hs = set()
        j = 0
        for i in range(len(nums)):
            if nums[i] not in hs:
                hs.add(nums[i])
                nums[i],nums[j] = nums[j],nums[i]
                j +=1
            
        return j
