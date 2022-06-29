name = input("What is your name? ")
age = int(input(f"What is your age {name}? "))

if 18 <= age <= 30:
    print(f"Welcome to the holiday {name} ! You are invited!")
else:
    print(f"""We are truly sorry {name}, you unfortunately cannot attend this trip""")