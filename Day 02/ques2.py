# Write a program that:
# Takes 5 numbers from user
# Stores them in a list
# Prints the list

numbers = []

for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)

print(numbers)
