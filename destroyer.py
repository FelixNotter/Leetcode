from collections import Counter
t = int(input())
for _ in range(t):
    n  = int(input())
    robots = list(map(int,input().split()))
    robots.sort()
    last = robots[-1]
    count = [float("inf")]*(last+1)
    for num in robots:
        if count[num] == float("inf"):
            count[num] = 1
        else:
            count[num] += 1
    broken = False
    for i in range(len(count)-1):
        if count[i] < count[i+1] or count[i] == float("inf"):
            broken = True
            break
    if not broken:
        print("YES")
    else:
        print("NO")
