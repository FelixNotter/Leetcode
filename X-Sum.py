t = int(input())
def solve():
    n,m = list(map(int,input().split()))
    board = []
    for _ in range(n):
        board.append(list(map(int,input().split())))
    
    def diagonalSum(board,row,col):
        r = row
        c = col
        currentSum = 0
        while c >= 0 and c < m and r >= 0 and r < n:
            currentSum += board[r][c]
            c -=1
            r-=1
        r = row
        c = col
        while c >= 0 and c < m and r >= 0 and r < n:
            currentSum += board[r][c]
            c +=1
            r-=1
        r = row
        c = col
        while c >= 0 and c < m and r >= 0 and r < n:
            currentSum += board[r][c]
            c -=1
            r+=1
        r = row
        c = col
        while c >= 0 and c < m and r >= 0 and r < n:
            currentSum += board[r][c]
            c +=1
            r+=1
        r = row
        c = col
        currentSum -= board[r][c]*3
        return currentSum
    maxSum = float("-inf")
    for r in range(n):
        for c in range(m):
            maxSum = max(maxSum,diagonalSum(board,r,c))
    print(maxSum)
for _ in range(t):
    solve()
