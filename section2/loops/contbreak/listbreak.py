shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "albatross"

# this is how to declare a variable without a value
# java - public int abcHello;
# python - abc_hello = None
found_at = None

# for index in range(6):
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

if item_to_find in shopping_list:
    # java list.getIndex(item)
    found_at = shopping_list.index(item_to_find)

# if the albatross index is not found - which in this case it is not - then print that it isn't found
# but if the index is found and has a value other than none, print it

if found_at is not None:
    print(f"Item found at {found_at}")
else:
    print(f"{item_to_find} is not found")

print(f"Item found at position {found_at}")