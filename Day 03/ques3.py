# Takes 6 numbers from the user
# Stores them in a list
# Creates a new list containing only the even numbers
# Prints the new list

a= []

for i in range(6):
    b = int(input("Enter number: "))
    a.append(b)

even_a = []

for i in range(len(a)):
    if a[i] %2 == 0:
        even_a.append(a[i])

print(f"List:\n{a}")
print(f"Even list:\n{even_a}")


# numbers = []

# for i in range(6):
#     num = int(input("Enter number: "))
#     numbers.append(num)

# even_numbers = []

# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)

# print("List:", numbers)
# print("Even list:", even_numbers)