class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        while l <= r:
            m = (l+r)//2
            print(m)
            if nums[m] == target:
                print(m)
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r = m -1
        return -1