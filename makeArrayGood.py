t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a = [[n,i] for i,n in enumerate(a)]
    a.sort()
    p = 0
    res = []
    for i in range(1,len(a)):
        
        n = a[i][0]//a[i-1][0]

        new = (n+1)*a[i-1][0]
        if a[i][0] % a[i-1][0] != 0:
            p+=1
            res.append((a[i][1]+1,new-a[i][0]))
            a[i][0] = new
    print(p)
    for num in res:
        print(*num)
        
        
