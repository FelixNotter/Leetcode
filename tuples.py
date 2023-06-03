# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
seen = {}
res = []
for i in range(N):
    word = input()
    if word in seen:
        seen[word] += 1
    else:
        seen[word] = 1
for key in seen:
    res.append(str(seen[key]))
print(len(seen))
print(" ".join(res))
    
