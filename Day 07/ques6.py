# Write a program that:
# takes a string
# counts how many vowels and consonants separately
# Example:
# hello → vowels: 2, consonants: 3

text = input("Enter a string: ")
vowels = 0
consonants = 0

for ch in text:
    if ch.isalpha():
        if ch in "aeiouAEIOU":
            vowels += 1
        else:
            consonants += 1

print(f"Vowels = {vowels}\nConsonants = {consonants}")
