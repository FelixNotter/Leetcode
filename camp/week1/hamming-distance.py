class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        number = x^y
        ans = 0
        while number: 
            if number &1 == 1:
                ans+=1
            number = number>>1
            
        return ans