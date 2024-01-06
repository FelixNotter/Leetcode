def solve():
    n = int(input())
    a = list(map(int,input().split()))
    diff = False
    for i in range(1,len(a)):
        if a[i]%2 != a[i-1]%2:
            diff = True
    if diff:
        a.sort()
    return a
 
 
 
 
print(*solve())
