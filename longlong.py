def solve():
    n = int(input())
    nums = list(map(int,input().split()))
    nums.append(1)
    count = 0
    res = 0
    negs = 0
    for i in range(n+1):
        res+=abs(nums[i])
        if nums[i] < 0:
            negs+=1
        if i-1>=0 and nums[i] > 0 and nums[i-1]<=0:
            if negs > 0:
                count+=1
                negs = 0
    return (res-1,count)
t = int(input())
for _ in range(t):
    print(*solve())
