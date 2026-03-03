# Write a program that:
# Takes 3 numbers
# Stores them in a list
# Prints the sum of the list elements
# (You must use a loop to calculate the sum. No sum() shortcut.)

num = []
sum = 0

for i in range(3):
    x = int(input("Enter number: "))
    num.append(x)
    sum += x

print(num)
print(f"Sum = {sum}")
