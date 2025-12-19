book = "  natURe   "
# print("Right:",book.rstrip(),"Z")
# print("Left:",book.lstrip(),"Z")
# print("Both:",book.strip(),"Z")

book = book.strip()

# Uppercase - NATURE
output = book.upper()
print("Uppercase:",output)
# Lowercase - nature
print("Lowercase:",book.lower())

# Capitalize - Nature
# first char - uppercase
# print("First char:",book[0])
# remaining chars - lowercase
# print("All but not first:",book[1:])


print("Capitalize:",book[0].upper() + book[1:].lower())
print("Capitalize:",book.capitalize())

print("Book:",book)