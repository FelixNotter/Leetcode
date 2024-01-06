def solve():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.append(float("inf"))
    a.sort()
    if k==0:
        return a[0]-1 if a[0] != 1 else -1
    
    idx = k-1
    if (a[idx+1] == a[idx]):
        return -1
    return a[idx]
 
 
 
 
 
print(solve())
