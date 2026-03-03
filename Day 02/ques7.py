# Write a program that:
# Takes 5 numbers from user
# Stores in list
# Finds the smallest number (without using min())
# Prints it

a = []

for i in range(5):
    b = int(input("Enter number: "))
    a.append(b)

min = a[0]

for i in range(1, len(a)):
    if a[i] < min:
        min = a[i]

print(a)
print(f"Minimum element in the list is {min}")
