q = int(input())
for _ in range(q):
    friends = list(map(int,input().split()))
    friends.sort()
    a,b,c = friends
    if c == b or a == b:
        if a == b and b != c and c-b > 1:
            a+=1
            b+=1
            c-=1    
        elif b == c and b != a and b - a > 1:
            b-=1
            c-=1
            a+=1
        elif a == b and b != c and c-b < 2:
            c-=1 
        elif b == c and b != a and b - a < 2:
            a+=1
        total = abs(c-a) + abs(b-a) + abs(c-b)
        print(total)
    elif a < b and c > a:
        a += 1
        c -= 1
        print(2*(c-a))
