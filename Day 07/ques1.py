# Write a program that:
# takes a string
# counts how many digits are in it
# Example:
# input: "a1b2c3"
# output: 3

name = input("Enter your name: ")
count = 0 

for ch in name:
    if ch in "1234567890":
        count+=1
    
print(f"Num of digits in string: {count}")
