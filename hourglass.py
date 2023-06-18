class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        l = 0
        r = 3
        t = 0
        b = 3
        maxSum = -1
        
        while b <= len(grid):
            while r <= len(grid[0]):
                matrix = [[grid[j][i]  for i in range(l,r) ]for j in range(t,b) ]
                print(matrix)
                maxSum = max(maxSum,self.computeSum(matrix))
                l +=1
                r +=1
            l = 0
            r = 3
            t += 1
            b += 1
        return maxSum



    def computeSum(self,grid):
        total = sum(grid[0]) + sum(grid[2]) + grid[1][1]
        return total 
