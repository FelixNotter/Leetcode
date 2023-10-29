class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        def flip(l,r):
            while l <= r:
                arr[l],arr[r] = arr[r],arr[l]
                l+=1
                r-=1
        
        for i in range(n):
            max_ = arr[0]
            idx = 0
            for j in range(n-i):
                if arr[j] >= max_:
                    max_ = arr[j]
                    idx = j
            res.append(idx+1)
            flip(0,idx)
            res.append(n-i)
            flip(0,n-1-i)
        
        return res

        