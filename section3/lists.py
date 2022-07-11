# a list is enclosed in square brackets in python

computer_parts = ["computer", 
                  "monitor", 
                  "keyboard", 
                  "mouse", 
                  "mousepad"]

for part in computer_parts:
    print(part)

print()
print(computer_parts[2])

# slicing a list
print(computer_parts[0:3])
print(computer_parts[-1])

# strings are immutable - they cannot be modified or changed
# lists are mutable which means they can be modified or changed

another_list = computer_parts

print(id(computer_parts))
print(id(another_list))

computer_parts += ["goodies"]
print(id(computer_parts))

# you cannot modify the value of immutable objects

a = b = c = d = e = another_list

# a, b, c, d, e just bound the same object (reference to another variable)

# duplicating the object (Same object) to different variables

print("\n")

print(a)
print("Appending cream...")
b.append("Cream")

print(c)
print(d)

# no matter which of the lists we use, its the same reference to the original [another_list]
# theres numerous aliases
