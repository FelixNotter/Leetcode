n = int(input())
arr1 = [[" "]*(n+1-(i)) + [j for j in range(i)] for i in range(n+2)]


for i  in range(1,len(arr1)):
    s = " ".join(map(str,arr1[i]))
    reverse = s[::-1]
    reverse[1:]
    s = s + reverse[1:].rstrip()
    print(s)
for i  in range(len(arr1)-2,0,-1):
    s = " ".join(map(str,arr1[i]))
    reverse = s[::-1]
    reverse[1:]
    s = s + reverse[1:].rstrip()
    print(s)
