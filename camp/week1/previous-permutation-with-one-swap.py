class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        flag = False
        idx = -1
        for i in range(len(arr)-1,-1,-1):
            if i-1>= 0 and arr[i] < arr[i-1]:
                flag = True
                idx = i-1
                break
    
        if not flag:
            return arr
        print(arr[idx])
        j = -1
        max_ = 0


        for i in range(len(arr)-1,idx,-1):
            if arr[i] >= max_ and arr[i] < arr[idx]:
                max_ = arr[i]
                j = i
        arr[idx],arr[j] = arr[j],arr[idx]
        return arr


        

        