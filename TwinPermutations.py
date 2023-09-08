def solve():
    n = int(input())
    a = list(map(int,input().split()))
    maxi = max(a)+1
    res = []
    for num in a:
        res.append(maxi-num)
    return res

t = int(input())
for _ in range(t):
    print(*solve())
