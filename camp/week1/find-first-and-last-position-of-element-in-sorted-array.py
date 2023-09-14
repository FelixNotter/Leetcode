class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(target):
            l = 0
            r = len(nums)
            while l < r:
                m = l+(r-l)//2
                if nums[m] >=target:
                    r = m
                else:
                    l = m+1
            return l
        r = search(target)
        l = search(target+1)
        if r == l:
            return [-1,-1]
        return [r,l-1]
        