def solve():
    n,m = map(int,input().split())
    
    a = "".join(["5"]*300+["5"])
    b = "".join(["4"]*300+["5"])
    return [int(a),int(b)]




print(*solve())
