# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

N_M = input().split()
N = int(N_M[0])
M = int(N_M[1])
hmap = defaultdict(list)
for i in range(N):
    letter = input()
    hmap[letter].append(str(i+1))
for j in range(M):
    word = input()
    if hmap[word]:
        print(" ".join(hmap[word]))
    else:
        print(-1)
            

