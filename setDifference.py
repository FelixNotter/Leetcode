# Enter your code here. Read input from STDIN. Print output to STDOUT
E = int(input())
english = input().split()
F = int(input())
french = input().split()
english_only = set(english) - set(french)
print(len(english_only))

