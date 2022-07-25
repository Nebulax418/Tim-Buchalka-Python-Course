# sort_lister.py

# even list
even = [2, 4, 6, 8]

# odd list
odd = [1, 3, 5, 7]

# EXTENDS THE EVEN LIST - does not combine them
# to combine lists use the + operator
# makes a big unsorted list
even.extend(odd)
print(even)

# newline
print("")

# doing some sorting with lists
even.sort(reverse = True)
print(even)


# doing something new ------------------------------------
print("-----------------")

abc = [1, 2, 3, 4, 5]
cba = [2, 5, 8, 9]

# joining the two lists and creating a new variable with it
new_list = abc + cba

print(new_list)

# sort operations
new_list.sort(reverse=True)
print(new_list)



# these ways are how to create a sorted list without copying it
# the sort method does not make a copy of a list
# the sort method only does it in-place

