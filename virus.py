def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
 
    segment = [n-a[-1]+a[0]-1]
    for i in range(1,m):
        segment.append(a[i]-a[i-1]-1)
    
    segment.sort(reverse=True)
    time = 0
    saved = 0
    
    for i in range(len(segment)):
        uninfected = segment[i] - 2*time
        if uninfected > 2:
            saved+= uninfected -1
            time+=2
        else:
            if uninfected > 0:
                saved +=1
                time+=1
    return n-saved
 
 
 
 
 
t = int(input())
for _ in range(t):
    print(solve())
