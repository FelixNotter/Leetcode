t = int(input())

for _ in range(t):
    n = int(input())
    nums1 = list(map(int,input().split()))
    nums2 = list(map(int,input().split()))
    nums1.sort()
    nums2.sort()
    found = False
    for i in range(n):
        if nums1[i] != nums2[i] and nums1[i] + 1 != nums2[i]:
            found = True
            print("NO")
            break
    if not found:
        print("YES")
