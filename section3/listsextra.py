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
