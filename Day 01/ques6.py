# Write a program that:
# Takes a number n
# Prints the multiplication table of n from 1 to 10

n = int(input("Enter number: "))

for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")
