from collections import Counter
t = int(input())
for _ in range(t):
    n,c = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    planets = Counter(nums)
    ans = 0
    for k,v in planets.items():
        if v >= c : 
            ans +=c
        else:
            ans +=1*v
    print(ans)
