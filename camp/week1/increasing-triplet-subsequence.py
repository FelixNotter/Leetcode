class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = nums[0]
        b = float("inf")
        for i in range(len(nums)):
            if nums[i] > b:
                return True
            if nums[i] > a:
                b = nums[i]
            if nums[i] < a:
                a = nums[i]
        return False
        