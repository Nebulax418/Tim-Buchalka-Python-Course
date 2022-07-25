empty_list = []

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]

numbers = even  + odd

print(numbers)


# where enumerate shines
for i, item in enumerate(numbers):
    if i == 0:
        #if item[i] == 0
        print(item)
        

# sorting the numbers with a NEW list
sorted_numbers = sorted(numbers)

print(sorted_numbers)

# check by printing numbers
print(numbers)


#.sort() to sort the exisiting list
numbers.sort()
print(numbers)

# sorting strings?

# you can also make a sorted variable string
digits = sorted("123456789")
print(digits)

# we can use the list function to create any list from an iterable
creation = list("abcd")
print(creation)

# creating lists using list()

# copying/duplicating the numbers list
# they are not the list
more_poo = list(numbers)
print(more_poo)

# check if they are the same by using is or printing them out
print(more_poo is numbers) # returns false

# use == if the elements inside the lists are in the same order
# use 'is' if the two variables are reffering to the same list

# has the same elements though
print(numbers)

# another way to copy a list is to use a slice
# python 2
another_more = numbers[:]
print(another_more)

# there is 12 different ways to copy a list
# the most efficient way is to use the copy method

good_copy = numbers.copy()
print(good_copy)
