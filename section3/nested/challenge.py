menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# for meal in menu:
#     # starting from the end and going to 1
#     for index in range(len(meal) - 1, -1, -1):
#         if meal[index] == "spam":
#             del meal[index]
    
#     print(meal)  

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item)
    
    print()                     


idi = [0, 1, 2, 3, 4] 

# getting the value at index 0
del idi[0]

print(idi)

print(idi[0])

"""
for item in list:
    if item == 'x':
        # never use remove in a for loop
        list.remove(item)

USE A COPY OF THE LIST

for item in list[:]:
    if item == 'x':
        list.remove(item)

"""