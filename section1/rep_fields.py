# every single datatype can be coerced into a string representation
# this is using the str function

age = 16

myList = []

# convert int to str
print("My age is " + str(age) + " years")

# this can get tedious, python 3.6 and higher can be formatted
# using .format methods

print("My age is {0} years".format(age))

# like %d in c programming
# there can be multiple values in the format list

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}"
      .format(31, "Jan", "Mar", "May", "July", "Aug", "Oct", "Dec"))

# replaced by the values consecutively using the .format() IN THIS CASE

# we do not need to go consecutively in order - I can do it like this too - but the values are coerced consecutively
print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {2}, May: {1}".format(31, 20, 303))


# we could do something similar with triple quotes

print("""
Jan: {2}, 
Feb: {0}, 
Mar: {2}, 
Apr: {2}, 
May: {1}""".format(31, 200, 20))