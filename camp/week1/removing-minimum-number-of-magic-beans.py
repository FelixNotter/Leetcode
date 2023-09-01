class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()

        res= float("inf")
        total = sum(beans)
        for i in range(len(beans)):
            res = min(res,total - (len(beans) - i)*beans[i])
            
        return res