'''                                    Solution
Assumptions:
1.We are guaranteed to have a at least a negative number in order to not get a non empty set
2.We are not guaranteed to have at least a positive number because two negatives can produce a positive product
3.We are guaranteed to have a zero in order to not get a non empty set
'''

t  = int(input())
contains = list(map(int,input().split()))
negatives = []
positives = []
zeroes = []
for num in contains:
    if num < 0:
        negatives.append(num)
    elif num > 0:
        positives.append(num)
    else:
        zeroes.append(num)

#We check to  see if we didnt have a positive input if we dont we will remove 2 negatives to the positive set
if len(positives) == 0:
    for _ in range(2):
        positives.append(negatives.pop())
#We the make sure that we dont have an even number of negatives since that gives us a positive product
if len(negatives) % 2 == 0:
    zeroes.append(negatives.pop()) 
print(len(negatives),*negatives)
print(len(positives),*positives)
print(len(zeroes),*zeroes)
