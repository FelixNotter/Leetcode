
t = int(input())

for i in range(t):
    input()
    n = []
    for _ in range(8):
        n.append(input())

    ROW = len(n)
    COL = len(n)
    for r in range(1,ROW-1):
        for c in range(1,COL-1):
            if n[r][c] == "#":
                if n[r-1][c-1] == "#" and n[r+1][c+1] == "#" and n[r - 1][c+1] == "#" and n[r+1][c-1] == "#":
                    print(r+1,c+1)
