t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    res = []
    l = 0
    r = len(nums)-1
    while l<r:
        res.append(nums[l])
        res.append(nums[r])
        l+=1
        r-=1
    if l == r:
        res.append(nums[l])
    print(*res)
