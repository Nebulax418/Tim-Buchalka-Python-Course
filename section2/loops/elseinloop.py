numbers = [23, 22, 31, 823, 643, 133]


# when the loop finds a value that is non-acceptable then the loop breaks out immideatly
# the else block executes

# the for loops acts like an if statmenet that just loops through some values,
# when triggered false, it executes the else statement

for i in numbers:
    if i % 8 == 0: 
        print("Reject the list")
        break
else:
    print("Not rejected")