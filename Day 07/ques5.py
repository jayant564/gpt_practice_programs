# Write a program that:
# takes a string
# counts frequency of each character
# Example:
# input: "aab"
# output: 
# a: 2
# b: 1

text = input("Enter a string: ")

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch in freq:
    print(ch, ":", freq[ch])