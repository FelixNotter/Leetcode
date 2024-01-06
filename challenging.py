def solve():
    n = int(input())
    a = list(map(int,input().split()))
    a.append(float("inf"))
    arr = []
    for i in range(1,len(a)):
        if a[i] == a[i-1]:
            continue
        arr.append(a[i-1])
    if len(arr) < 2:
        return "YES"
    count = 0
    if arr[0] < arr[1]:
        count +=1
    if arr[-1] < arr[-2]:
        count+=1
      
    
    for i in range(1,len(arr)-1):
        if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
            count+=1
            
    return "YES" if count == 1 else "NO"
        
 
 
 
 
t = int(input())
for _ in range(t):
    print(solve())
