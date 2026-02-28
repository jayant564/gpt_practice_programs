# Write a program that:
# Takes a number
# Prints:
# "Positive" if number > 0
# "Negative" if number < 0
# "Zero" if number == 0

n = int(input("Enter number: "))

if n==0:
    print("You entered 0")
elif n>0:
    print("Positive")
else:
    print("Negative")
