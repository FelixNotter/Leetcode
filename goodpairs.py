t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    nums = [(n,i) for i,n in enumerate(nums)]
    nums.sort()
    print(nums[0][1]+1,nums[-1][1]+1)
