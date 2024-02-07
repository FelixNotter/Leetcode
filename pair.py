def solve():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = [a[i]-b[i] for i in range(n)]
    c.sort()
    l = 0
    r = len(c)-1
    ans = 0
    while l < r:
        if c[l] + c[r] > 0:
            ans+=(r-l)
            r-=1
        else:
            l+=1 
    return ans





print(solve())
