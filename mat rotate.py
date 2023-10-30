def rotate(x):
    x[0][0],x[0][1] = x[0][1],x[0][0]
    x[1][0],x[1][1] = x[1][1],x[1][0]
    x[0][0],x[1][1] = x[1][1],x[0][0]
    return x
 
def check(x):
    return x[0][0] > x[0][1] and x[1][0] > x[1][1] and x[0][0] > x[1][0] and x[0][1] > x[1][1]
def solve():
    res = []
    for _ in range(2):
        s1 = list(map(int,input().split()))
        res.append(s1)
    for _ in range(4):
        if check(res):
            return "YES"
        res = rotate(res)
    return "NO"
 
    
 
 
t = int(input())
for _ in range(t):
    print(solve())
