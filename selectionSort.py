class Solution: 
    
    def selectionSort(self, arr,n):
        #code here
        idx,minimum = 0,arr[0]
        for i in range(len(arr)):
            minimum = arr[i]
            for j in range(i+1,len(arr)):
                if arr[j] < minimum:
                    minimum = arr[j]
                    idx = j
            if arr[i] > minimum:
                arr[i],arr[idx] = arr[idx],arr[i]
        return arr
