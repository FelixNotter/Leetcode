def p(n):
    ans = 0
    while n%2 == 0:
        ans+=1
        n = n//2
    return ans 

def solve():
    n = int(input())
    a = list(map(int,input().split()))
    idx = []
    nums = []
    for i in range(n):
        idx.append(p(i+1))
        nums.append(p(a[i]))

    if sum(nums) >= n:
        return 0
    idx.sort(reverse = True)
    ops = 0
    add = sum(nums)

    for i in range(len(idx)):
        ops+=1
        add+=idx[i]
        if add >= n:
            return ops
    return -1
     

        




t = int(input())
for _ in range(t):
    print(solve())
