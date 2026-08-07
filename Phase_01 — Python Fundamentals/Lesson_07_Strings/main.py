# ==================================================
# Lesson 07 - Strings
# Part 1: Creating Strings with f-Strings
# ==================================================

name = "Ngọc"
age = 25

# Old way: concatenate strings using the + operator.
# This works, but it becomes difficult to read when many variables are involved.
greeting_old = "Xin chào " + name + ", bạn " + str(age) + " tuổi"

# Modern way: use an f-string.
# Add the letter 'f' before the quotation marks and place variables inside {}.
greeting_new = f"Xin chào {name}, bạn {age} tuổi"

print(greeting_old)
print(greeting_new)

# You can also evaluate expressions directly inside {}.
print(f"Năm sau bạn sẽ {age + 1} tuổi")

# Format numbers inside an f-string.
# :.2f means "display the number with 2 decimal places".
price = 19.98765
print(f"Giá: {price:.2f} EUR")


# ==================================================
# Part 2: String Slicing
# ==================================================

text = "Fachinformatiker"

# Slice from index 0 up to (but not including) index 5.
print(text[0:5])      # "Fachi"

# If the start index is omitted, Python starts from the beginning.
print(text[:4])       # "Fach"

# If the end index is omitted, Python continues to the end of the string.
print(text[4:])       # "informatiker"

# Negative indexes count from the end of the string.
print(text[-4:])      # "iker"

# The third value is the step.
# A step of 2 means "take every second character".
print(text[::2])

# A negative step reverses the string.
print(text[::-1])     # "rekitamrofnihcaF"
