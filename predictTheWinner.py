class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def dfs(l,r,turn,s1,s2):
            if l > r:
                return s1>=s2
            ans1 = dfs(l+1,
            r,
            not turn,
            s1+nums[l] if turn else s1,
            s2+nums[l] if not turn else s2
            )
            ans2 = dfs(l,
            r-1,
            not turn,
            s1+nums[r] if turn else s1,
            s2+nums[r] if not turn else s2
            )
            if turn:
                return ans1 or ans2
            return ans1 and ans2
        return dfs(0,len(nums)-1,True,0,0)
     

         
        


        
