t = int(input())

for _ in range(t):
    array = []
    n = int(input())
    for i in range(1,n+1):
        array.append(2*i)
    print(*array)
