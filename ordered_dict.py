# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
N = int(input())
item_price = []
ordered_dict = OrderedDict()
for i in range(N):
    item_list = input()
    item_price.append(item_list.split())
for *name,price in item_price:
    full_name = " ".join(name)
    if full_name in ordered_dict:
        ordered_dict[full_name] += int(price)
    else:
        ordered_dict[full_name] = int(price)
for key,val in ordered_dict.items():
    print(key,val)
