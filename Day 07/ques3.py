# Write a program that:
# takes a string
# counts how many uppercase letters are in it

text = input("Enter a string: ")

count = 0

for ch in text:
    if ch.isupper():
        count += 1

print("Uppercase letters:", count)