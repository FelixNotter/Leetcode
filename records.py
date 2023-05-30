if __name__ == '__main__':
    res = []
    n = int(input())
    #building the records Array
    for _ in range(n):
        cur = []
        name = input()
        score = float(input())
        cur.append(name)
        cur.append(score)
        res.append(cur)
    #sorting the Array based on scores
    sorted_res = sorted(res,key = lambda a: a[1])
    second_lowest = 0
    #computing the runner up score
    for i in range(1,len(sorted_res)):
        if sorted_res[i-1][1] != sorted_res[i][1]:
            second_lowest = sorted_res[i][1]
            break
        
        
    final = []
    #Adding all the runner ups to an Array
    for n,s in sorted_res:
        if second_lowest == s:
            final.append(n)
    # Sorting the runner ups 
    final.sort()
    #printing all runner ups
    for p in final:
        print(p)
