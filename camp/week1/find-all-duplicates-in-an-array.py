class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while i < len(nums):
            if nums[i]-1 != i:
                if nums[i] == nums[nums[i]-1]:
                    i+=1
                else:
                    nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
            else:
                i+=1
        for i in range(len(nums)):
            if nums[i]-1 != i:
                ans.append(nums[i])
        return ans
        