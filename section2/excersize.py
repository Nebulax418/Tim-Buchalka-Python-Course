quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

capital_extract = ""

for char in quote:
    if char.isupper():
        # appends the uppercase character to the string
        capital_extract+=char


print(capital_extract)