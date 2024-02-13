class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans = 0
        second = []
        for i in range(len(costs)):
            second.append([abs(costs[i][1]-costs[i][0]),costs[i][0],costs[i][1]])

        second.sort(reverse = True)
   
        a = 0
        b = 0
        n = len(costs)//2
        for i in range(len(costs)):
            if a < n and b < n:
                if second[i][1] < second[i][2]:
                    a+=1
                    ans+=second[i][1]
                else:
                    b+=1
                    ans+=second[i][2]
            elif a == n:
                b+=1
                ans+=second[i][2]
            else:
                a+=1
                ans+=second[i][1]
            
        return ans
        