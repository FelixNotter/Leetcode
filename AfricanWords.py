n,m = map(int,input().split())
board = []
for i in range(n):
    board.append(input())
flat = []
for row in board:
    for letter in row:
        flat.append(letter)

rows = {}
cols = {}
for i in range(len(flat)):
    if (flat[i],i%m) not in cols:
        cols[(flat[i],i%m)] = 1
    else:
        cols[(flat[i],i%m)] += 1
    if (flat[i],i//m) not in rows:
        rows[(flat[i],i//m)] = 1
    else:
        rows[(flat[i],i//m)] += 1

for i in range(len(flat)):
    if cols[flat[i],i%m] > 1 or rows[flat[i],i//m] > 1:
        flat[i] = "."
word = []
for char in flat:
    if char != ".":
        word.append(char)
print("".join(word))
