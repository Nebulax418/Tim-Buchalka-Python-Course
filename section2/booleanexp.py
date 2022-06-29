# not is used to reverse a boolean value
# like the not logical gate

day = "Monday"
temperature = 30
raining = False


# this does not directly say anything so don't read it like english - operator precedence is always first
# use parantheses
if (day == "Saturday" and temperature > 27) or not raining:
    print("Go swimming")
else:
    print("Stay home and learn python")
    
# boolean operator precedence

# or before and
# and before not
# or before not

# so the precedence is always going to be:

# OR
# AND
# NOT
