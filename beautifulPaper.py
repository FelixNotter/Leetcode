t = int(input())
for i in range(t):
    first = list(map(int,input().split()))
    second = list(map(int,input().split()))
    first.sort()
    second.sort()
    if  first[1] == second[1] and first[0] + second[0] == first[1]:
        print("YES")
    elif first[0] == second[0] and first[1] + second[1] == first[0]:
        print("YES")
    else:
        print("NO")
