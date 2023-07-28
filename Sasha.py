t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    res = 0
    nums.sort()
    l = 0
    r = len(nums)-1
    while l<r:
        res +=abs(nums[r]-nums[l])
        r-=1
        l+=1
    print(res)
