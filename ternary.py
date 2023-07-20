t = int(input())
for _ in range(t):
    s = input()
    hmap = {}
    l = 0
    cur = 0
    res = float("inf")
    for r in range(len(s)):
        if s[r] not in hmap:
            cur +=1
            hmap[s[r]] = 1
        else:
            if not hmap[s[r]]:
                cur +=1
            hmap[s[r]] +=1      
        while cur == 3:
            res = min(res,r-l+1)      
            hmap[s[l]] -= 1          
            if not hmap[s[l]]:
                cur -= 1
            l+=1   
    if res == float("inf"):res = 0
    print(res)
