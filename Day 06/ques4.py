# Write a program that:
# takes a string
# counts how many consonants are in it
# (letters that are NOT vowels)

text = input("Enter a string: ")

count = 0

for ch in text:
    if ch.isalpha() and ch not in "aeiouAEIOU":
        count += 1

print("Number of consonants:", count)
