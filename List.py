import random as rd
from functools import reduce

my_list = [rd.randint(0, 100) for k in range(0, 10)]


# print('Write a Python program to multiply all the items in a list: ')
# p = 1
# for k in my_list:
#     p = p*k
# print('WAY1: Product: ', p)
# print('WAY2: Product: ', reduce(lambda x, y: x*y, my_list))

# print('Write a Python program to sum all the items in a list'
#       , sum(my_list))
