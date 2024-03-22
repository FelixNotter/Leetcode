def solve():
    n = int(input())
    a = list(map(int,input().split()))
    lead = True
    zero = 0
    for i in range(n-1):
        if a[i]!= 0:
            lead = False
        if not lead and a[i] == 0:
            zero+=1
    return sum(a)-a[-1]+zero

    



t = int(input())
for _ in range(t):
    print(solve())
