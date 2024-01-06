def solve():
    s = input()
    res = []
    for i in range(8):
        res.append(input())

    for r in range(1,7):
        for c in range(1,7):
            if (res[r][c] == "#") and (res[r][c] == res[r-1][c-1]) and (res[r][c] == res[r-1][c+1]) and (res[r][c] == res[r+1][c-1]) and (res[r][c] == res[r+1][c+1]):
                return r+1,c+1




t = int(input())
for _ in range(t):
    print(*solve())
