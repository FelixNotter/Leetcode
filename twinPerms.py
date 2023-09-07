def solve():
    pairs = {}
    n = int(input())
    a = list(map(int,input().split()))
    prev = 0
    for i in range(len(a)):
        if a[i] - prev != 1:
            break
        prev = a[i]
        pairs[a[i]] = a[i]
    if i == len(a)-1:
        p = a[::-1]
        return p
    nums = a[i:]
    nums.sort()
    l = 0
    r = len(nums)-1
    while l <=r:
        pairs[nums[l]] = nums[r]
        pairs[nums[r]] = nums[l]
        l+=1
        r-=1
    res = []
    for num in a:
        res.append(pairs[num])
    return res

t = int(input())
for _ in range(t):
    print(*solve())
