# Write a function:
# Takes a list
# Adds number 10
# Returns new list WITHOUT modifying original

text = []
for i in range(10):
    j = input("Enter nums: ")
    text.append(j)

copy_text = text.copy()
copy_text[1] = "ABC"

print(f"{copy_text}")