def solve():
    a = input()
    b = input()
    memo = {}
    def recurse(x,y):
        if (x,y) in memo:
            return memo[(x,y)]
        if x == y:
            return True
        if len(x)%2 == 1: 
            return x == y
        a1,a2 = x[:len(x)//2],x[len(x)//2:]
        b1,b2 = y[:len(y)//2],y[len(y)//2:]
      
        memo[(x,y)] = (recurse(a1,b1) and recurse(a2,b2)) or (recurse(a1,b2) and recurse(a2,b1))
        return memo[(x,y)]
    if recurse(a,b):
        return "YES"
    return "NO"


print(solve())
