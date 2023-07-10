t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    nums.sort()
    count = 0
    for i in range(n-1):
        if abs(nums[i]-nums[i+1]) <=1:
            count +=1
    if len(nums) - count == 1:
        print("YES")
    else:
        print("NO")
