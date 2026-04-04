# Write a program that:
# takes a string
# checks if it is a palindrome
# Example:
# madam → Yes
# hello → No

str = input("Enter string: ")
str_rev = str[::-1]
if str == str_rev:
    print("Yes Palindrome")
else:
    print("Not Palindrome")
