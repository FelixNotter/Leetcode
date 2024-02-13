class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        ans = 0
        for i in range(len(arr)):
            if i-1>=0 and abs(arr[i]-arr[i-1]) > 1:
                ans+=1
                arr[i] = arr[i-1]+1
        return max(arr)
        