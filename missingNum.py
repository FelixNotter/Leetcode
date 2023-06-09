class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for index in range(len(nums)):
            if index != nums[index]:
                return index
            else:
                continue
        return nums[index] + 1 
