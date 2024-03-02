# Unpacking list/tuples
numbers = [1, 2, 3, 4, 5]									

*begin, last = numbers
print(begin)																# This will always return a list where the original one was list or tuple, from 1 to 4
print(last)

begin, *last = numbers
print(begin)																
print(last)																	# This will always return a list where the original one was list or tuple, from 2 to 5

begin, *middle, last = numbers

# Merging diff iterables into list
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}

new_list = [*my_tuple, *my_list, *my_set]
print(new_list)

# Merging two dicts
dict_a = {'a':1, 'b':2}
dict_b = {'c':3, 'd':4}
my_dict = {**dict_a, **dict_b}
print(my_dict)
