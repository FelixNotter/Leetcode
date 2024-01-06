def solve():
    s = input()
    s+="?"
    count = 1
    res = []
    seen = set()
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count+=1
        else:
            if count%2 == 1:
                if s[i-1] not in seen:
                    res.append(s[i-1])
                    seen.add(s[i-1])
            count = 1
    res.sort()
    return "".join(res)
    
 
 
 
t = int(input())
for _ in range(t):
    print(solve())
