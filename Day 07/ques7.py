# Write a program that:
# takes a string
# counts:
#   vowels
#   consonants
#   digits
#   spaces
# Example:
# Input: "Hello 123"
# Output:
#   Vowels = 2
#   Consonants = 3
#   Digits = 3
#   Spaces = 1

text = input("Enter a string: ")
vowels, consonants, digits, spaces = 0,0,0,0

for ch in text:
    if ch.isalpha():
        if ch in "aeiouAEIOU":
            vowels += 1
        else:
            consonants += 1
    elif ch.isalnum():
        if ch in '123456790':
            digits += 1
    else: 
        spaces += 1

print(f"Vowels = {vowels}\nConsonants = {consonants}\nDigits = {digits}\nSpaces = {spaces}")
