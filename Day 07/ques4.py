# Write a program that:
# takes a string
# removes all spaces
# prints the new string
# Example:
# input: "hello world"
# output: "helloworld"

text = input("Enter a string: ")

result = ""

for ch in text:
    if ch != " ":
        result += ch

print("Without spaces:", result)
