t = int(input())
for _ in range(t):
    n = int(input())
    cubes = list(map(int,input().split()))
    i = 0
    while i >= 0 and i < len(cubes)-1 and cubes[i] > cubes[i+1]:
        i+=1
    if i+1 == len(cubes):
        print("NO")
    else:
        print("YES")
    
   
