# Write a program that:
# Takes 5 numbers from user
# Stores in list
# Replaces every even number with 0
# Prints final list

a = []

for i in range(5):
    a2 = int(input("Enter number: "))
    if a2%2==0:
        a2 = 0
    a.append(a2)
        
print(a)

# numbers = []

# for i in range(5):
#     num = int(input("Enter number: "))
#     numbers.append(num)

# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         numbers[i] = 0

# print(numbers)