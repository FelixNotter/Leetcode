class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            curr = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    curr +=1
            res.append(curr)
        return res
