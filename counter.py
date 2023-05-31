# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X = int(input())
shoes = input()
shoe_list = shoes.split()
#Shoes Available
available_shoes = Counter(shoe_list)
total = 0
price_list = []
N = int(input())
#Build Price Array
for i in range(N):
    user = input()
    price_list.append(user.split())
for size,price in price_list:
    if available_shoes[size] > 0:
        total += int(price)
        available_shoes[size] -= 1
print(total)
