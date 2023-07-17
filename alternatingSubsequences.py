t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
 
    res = 0
    r = 0
 
    while r < len(nums):
        maximum = -float("inf")
        while r < len(nums) and nums[r] < 0:
            maximum = max(maximum,nums[r])
            r+=1
        res+= maximum if maximum != -float("inf") else 0
        maximum = -float("inf")
        while r < len(nums) and nums[r] > 0:   
            maximum = max(maximum,nums[r])
            r+=1
    
        res+= maximum if maximum != -float("inf") else 0
            
    print(res)
