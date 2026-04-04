# Write a program that:
# takes a string
# counts how many vowels are in it (a, e, i, o, u)

str1 = "I am learning python language."
count = 0
for ch in str1:
    if ch in 'aeiouAEIOU':
        count+=1

print(f"Number of vowels: {count}")
