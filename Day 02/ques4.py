# Write a program that:
# Creates list: [1, 2, 3, 4, 5]
# Changes every element to its square
# Prints the final list

a = [1, 2, 3, 4, 5]

for i in range(len(a)):
    a[i] = a[i] **2
print(a)
