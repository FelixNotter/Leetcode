t = int(input())
for _ in range(t):
    n,m = list(map(int,input().split()))
    board = []
    for i in range(n):
        board.append(list(input()))
    
    for r in range(n-1,-1,-1):
        for c in range(m-1,-1,-1):
            if board[r][c] == "*":
                i = r
                while i+1 < n and board[i+1][c] == '.':
 
                    board[i][c] = "."
                    board[i+1][c] = "*"
                    i+=1
 
 
    for row in board:
        print("".join(row))
    print()
