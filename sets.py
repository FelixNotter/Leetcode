# Enter your code here. Read input from STDIN. Print output to STDOUT
Set_A = set(input().split())
N = int(input())
ans = set()
for i in range(N):
    other = input().split()
    for char in other:
        if char not in Set_A:
            ans.add(False)
ans.add(True)
if False in ans:
    print(False)
else:
    print
