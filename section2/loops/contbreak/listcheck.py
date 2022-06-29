# a list is an ordered sequence of values enclosed with []

shopping_list = ["milk", "spam", "bread", "rice", "spinach", "cheese"]

# for item in shopping_list:
#     if item  != "spam":
#         print(f"Buy {item}")

# we don't like spam - let's use the continue keyword

for item in shopping_list:
    if item == "spam":
        continue # skip this iteration
    
    print(f"Buy {item}")
