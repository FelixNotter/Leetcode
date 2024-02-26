def isSet(l,n):
    return (n&(1<<(l)))

def solve():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    ans = ""
    
    for j in range(30,-1,-1):
        count = 0
        for i in range(n):
            if isSet(j,a[i]) == 0:
                count+=1
        if count <= k:
            ans = ans+"1"
            k-= count
        else:
            ans = ans+"0"
    return int(ans,2)








t = int(input())
for _ in range(t):
    print(solve())
