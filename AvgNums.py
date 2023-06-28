n = int(input())
array = list(map(int,input().split()))
total = sum(array)
indices = []
for i in range(n):
    if (total - array[i])/(n-1) == array[i]:
        indices.append(i+1)
print(len(indices))
print(*indices)
