# Write code to:
# Take a list
# Create a copy
# Modify the copy
# Show original is unchanged

text = []
for i in range(5):
    j = input("Enter text: ")
    text.append(j)

copy_text = text.copy()
copy_text[1] = "ABC"

print(f"Original: {text}")
print(f"Copy: {copy_text}")