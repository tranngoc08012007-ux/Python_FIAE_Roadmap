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
# ==================================================
# Part 3: Common String Methods
# ==================================================

raw_input = "  Nguyen Ngoc  "

# strip() removes leading and trailing whitespace.
# It does NOT remove spaces in the middle of the string.
clean_name = raw_input.strip()
print(f"'{clean_name}'")  # 'Nguyen Ngoc'

# split() breaks a string into a list, based on a separator.
# If no separator is given, it splits on whitespace by default.
full_name = "Nguyen Ngoc Tran"
parts = full_name.split(" ")
print(parts)  # ['Nguyen', 'Ngoc', 'Tran']

# join() does the opposite of split(): it combines a list into one string,
# placing the given separator between each item.
joined = "-".join(parts)
print(joined)  # 'Nguyen-Ngoc-Tran'

# upper() / lower() change the case of all letters in the string.
# Useful for normalizing data before comparison.
email = "Ngoc@Example.COM"
print(email.lower())  # 'ngoc@example.com'

# replace(old, new) substitutes every occurrence of "old" with "new".
sentence = "Tôi học Java"
print(sentence.replace("Java", "Python"))  # 'Tôi học Python'

# --- Exercise: cleaning and parsing raw location data ---
raw_data = "  Ho Chi Minh City, Vietnam  "

# Step 1: remove the extra whitespace around the whole string.
clean_data = raw_data.strip()

# Step 2: split into city and country using "," as the separator.
city, country = clean_data.split(",")

# Step 3: strip() each part again, because split() does not remove
# the whitespace that sits right next to the comma.
city = city.strip()
country = country.strip()

print(city.upper())  # "HO CHI MINH CITY"
print(country)        # "Vietnam"


# ==================================================
# Part 4: String Comparison
# ==================================================

# Strings are compared lexicographically: character by character,
# based on each character's Unicode code point.
print("apple" == "apple")   # True -> identical strings
print("apple" == "Apple")   # False -> comparison is case-sensitive

# When comparing with < or >, Python compares characters one by one
# until it finds a difference.
print("apple" < "banana")   # True -> 'a' comes before 'b'
print("Apple" < "apple")    # True -> uppercase letters have lower
                             # Unicode values than lowercase letters

# Because comparison is case-sensitive, it's common practice to
# normalize both sides with lower() (or upper()) before comparing
# user input.
user_input = "Munich"
target = "munich"
print(user_input.lower() == target.lower())  # True
