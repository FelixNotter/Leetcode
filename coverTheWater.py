def solve():
    n = int(input())
    s = input()
    s+="#"
    count = 0
    ans = 0
    for i in range(n+1):
        if s[i] == ".":
            count+=1
        else:
            if count > 2:
                return 2
            else:
                ans+=count
                count = 0
    return ans
        





t = int(input())
for _ in range(t):
    print(solve())
