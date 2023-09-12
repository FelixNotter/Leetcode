def solve():
    n,k = input().split()
    n,k = int(n),int(k)
    p = list(map(int,input().split()))
    count = 0
    for i in range(len(p)):
        if p[i]%k!=(i+1)%k:
            count+=1
    if count == 2:
        return 1
    elif count > 2:
        return -1
    else:
        return 0

t = int(input())
for _ in range(t):
    print(solve())
