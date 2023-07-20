n = int(input())
nums = list(map(int,input().split()))
nums.sort()
l = 0
res = 0
for r in range(len(nums)):
    while nums[r] - nums[l] > 5:
        l+=1
    res = max(res,r-l+1)
print(res)
