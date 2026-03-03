# Write a program that:
# Takes 5 numbers
# Counts how many numbers are positive
# Prints the count

a = []

for i in range(5):
    b = int(input("Enter number: "))
    a.append(b)

count = 0
for i in range(len(a)):
    if a[i] > 0:
        count += 1

print(f"Positive element in the list are {count}")
