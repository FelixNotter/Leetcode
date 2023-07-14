t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int,input().split()))
    maximum = max(s)
    s = [[n,i] for i,n in enumerate(s)]
    s.sort()
    res = [0]*len(s)
    for i in range(len(s)-1):
       
        if s[i][0] - maximum != 0:
            res[s[i][1]] = (s[i][0]- maximum)
    res[s[-1][1]] = -1*(s[-2][0] - maximum)
    
    print(*res)
