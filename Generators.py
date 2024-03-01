'''
 Generators are functions that return objects that can be iterated over
 Generates item one at a time and only when asked because of this they
 are much more memory efficient
'''

def mygenerator():
	yield 1
	yield 2
	yield 3

g = mygenerator()

#for i in g:
#	print(i)

# Getting values one at a time
value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)																# If you again print this then it will raise "StopIteration" error as now it has now next value after 3


# Using generator as input to other function which take iterables
print(sum(g))																# will now print 0 b/c of next() the generator has reached it end, so we got no values to add
print(sorted(g))															# will print empty list

# Another generator
def countdown(num):
	print("Starting")
	while num > 0:
		yield num
		num -= 1
	
cd = countdown(4)
value = next(cd)
print(next(cd))
print(next(cd))
print(next(cd))

# Advantages of using generators
# without a generator, the complete sequence has to be stored here in a list
def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
import sys
print(sys.getsizeof(firstn(1000000)), "bytes")								# Size -> 8448728

# with a generator, no additional sequence is needed to store the numbers
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
print(sys.getsizeof(firstn(1000000)), "bytes")								# Size -> 104

# Generators comprehension
my_generator = (i for i in range(10) if i % 2 == 0	)						# Similar to list comprehension except they use []
for i in my_generator:
	print(i)

# Converting generator object to list
l = list(my_generator)
