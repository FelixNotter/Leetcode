# Enter your code here. Read input from STDIN. Print output to STDOUT
E = int(input())
english = set(input().split())
F = int(input())
french = set(input().split())

both = french.union(english)
print(len(both))
