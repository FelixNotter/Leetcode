class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nums = [i for i in range(int(sqrt(c))+1)]
        l = 0
        r = len(nums)-1
        while l<= r:
            cur = (nums[l]**2)+(nums[r]**2)
            if cur == c:
                return True
            if cur > c:
                r-=1
            else:
                l+=1
        return False
