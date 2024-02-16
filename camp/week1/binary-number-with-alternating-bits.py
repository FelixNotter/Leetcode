class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        one = 0
        zero = 0
        while n:
            if n&1 == 1:
                one+=1
                zero = 0
            else:
                zero+=1
                one = 0
            if one > 1 or zero > 1:
                return False
            n = n>>1
        return True
        