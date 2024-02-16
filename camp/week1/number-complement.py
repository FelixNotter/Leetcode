class Solution:
    def findComplement(self, num: int) -> int:
        res = []
        while num:
            if num&1 == 0:
                res.append(1)
            else:
                res.append(0)
            num = num >> 1
        ans = 0
        for i in range(len(res)):
            ans+=(res[i]<<i)
        return ans