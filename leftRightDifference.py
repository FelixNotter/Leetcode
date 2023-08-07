class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = [0]*len(nums)
        ans = []
        for i in range(1,len(nums)):
            leftSum[i] = leftSum[i-1]+nums[i-1]
        rightSum = [0]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            rightSum[i] = rightSum[i+1]+nums[i+1]
        for i in range(len(nums)):
            curr = abs(leftSum[i] - rightSum[i])
            ans.append(curr)
        return ans
