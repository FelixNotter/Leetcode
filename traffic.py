def solve():
    n,c = input().split()
    s = input()
    s+=s
    res = 0
    n = int(n)
    seen = False
    last = -1
    res = 0
    for i in range(len(s)-1,-1,-1):
        if s[i] == "g":
            last = i
        elif s[i] == c:
            res = max(res,last-i)
    return res
 
 
    
   
 
    
 
 
 
 
t = int(input())
for _ in range(t):
    print(solve())
