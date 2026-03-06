# Write a program that:
# Takes 5 numbers
# Takes another number (target)
# Checks if target exists in the list
# Prints "Found" or "Not Found"

a = []

for i in range(5):
    b = int(input("Enter number: "))
    a.append(b)

target = int(input("Enter number to search: "))

for i in range(len(a)):
    if a[i] == target:
        print("Found")
        break
else:
    print("Not Found")
    
