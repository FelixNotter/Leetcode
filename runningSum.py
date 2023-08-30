class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = [nums[0]]
        for index in range(1,len(nums)):
            added = running_sum[-1] + nums[index]
            running_sum.append(added)
        return running_sum
