available_parts = ["Computer",
                   "Monitor",
                   "HDMI Cable",
                   "Mouse",
                   "Mousepad",
                   "Gaming headset",
                   "Keyboard",
                   "Gaming char"]

print(available_parts)

available_parts[3] = "trackball"
print(available_parts)

print()
print(available_parts[3:])

# strange things
available_parts[3:] = "trackball"
print(available_parts)

# adding a new element correctly this time 
# elements 3 and onwards were replaced with trackball
available_parts[3:] = ["trackball"]
print(available_parts)


