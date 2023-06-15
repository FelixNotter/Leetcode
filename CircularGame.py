class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        #initialising both the array of and the pointer used to keeptrack
        nums = [i+1 for i in range(n)]
       
        i = 0
        #loop until only one person is left in the circle
        while len(nums) != 1:
            
            for _ in range(k):
                i+=1
            i = (i-1) % len(nums)
           
            nums.pop(i)
        return nums[0]
