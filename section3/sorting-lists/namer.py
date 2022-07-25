names = ["Kohn", "terry", "Chad", "eric", "Marko"]

# sorts the list alphabetically not regarding captials
# note: captials take precedence over uncaptialized letters
names.sort(key=str.casefold)

print(names)