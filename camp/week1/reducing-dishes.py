class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        ans = float("-inf")
        for i in range(len(satisfaction)):
            count = 1
            cur = 0
            for j in range(i,len(satisfaction)):
                cur+=satisfaction[j]*count
                count+=1
            ans = max(ans,cur)
        return max(0,ans)



        