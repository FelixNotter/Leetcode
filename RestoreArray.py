t = int(input())
def solve():
    n = int(input())
    b = list(map(int,input().split()))
    #initialising the a array
    a = [float('inf')]*n
    for i in range(len(b)):
        if b[i] < a[i]:
            a[i] = b[i]
        if b[i] < a[i+1]:
            a[i + 1] = b[i]
    return a
for _ in range(t):
    a = solve()
    print(*a)
