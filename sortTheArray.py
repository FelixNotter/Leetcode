n = int(input())
nums = list(map(int,input().split()))
end = len(nums)-1
sorted_nums = sorted(nums)
printed = False
if nums == sorted_nums:
    printed = True
    print("yes")
    print(1,1)
while end >= 0 and nums[end] > nums[end - 1]:
    end -= 1
start = 0
while start < len(nums)-1 and nums[start] < nums[start + 1]:
    start+=1
l = start
r = end
while l < r:
    nums[l],nums[r] = nums[r],nums[l]
    l+=1
    r -= 1
if nums != sorted_nums:
    print("no")
else:
    if not printed:
        print("yes")
        print(start+1,end+1)
