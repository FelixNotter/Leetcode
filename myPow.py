class Solution:
    def myPow(self, x: float, n: int) -> float:
     
        exp = abs(n)
        def helper(x,p):
           
            if p == 0:
                return 1
            half = helper(x,p//2)
            if p % 2 == 0:
                return half*half 
            else:
                return x*half*half 
                
        ans = helper(x,exp)
        if n < 0:
            return 1/ans
        return ans
        
