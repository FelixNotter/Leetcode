if __name__ == '__main__':
    import random
    N = int(input())
    

    y = []
    for i in range(N):
        instructions = input().split()
        if instructions[0] == "append":
            y.append(int(instructions[1]))
        if instructions[0] == "remove":
            y.remove(int(instructions[1]))
        if instructions[0] == "insert":
            y.insert(int(instructions[1]),int(instructions[2]))
        if instructions[0] == "sort":
            y.sort()
        if instructions[0] == "pop":
            y.pop()
        if instructions[0] == "print":
            print(y)
        if instructions[0] == "reverse" :
            y.reverse()
 
