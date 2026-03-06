# Write a program that:
# Takes 5 numbers
# Finds the second largest number (without sorting, without max())

a = []

for i in range(5):
    b = int(input("Enter number: "))
    a.append(b)

max = a[0]
max2 = a[0]

for i in range(1, len(a)):
    if a[i] > max:
        max2 = max
        max = a[i]

    elif a[i] > max2 and a[i] != max:
        max2 = a[i]

print(a)        
print(f"Maximun element is {max}")
print(f"Second Max element in the list is {max2}")


# numbers = []

# for i in range(5):
#     num = int(input("Enter number: "))
#     numbers.append(num)

# largest = numbers[0]
# second_largest = numbers[1]

# if second_largest > largest:
#     largest, second_largest = second_largest, largest

# for i in range(2, len(numbers)):

#     if numbers[i] > largest:
#         second_largest = largest
#         largest = numbers[i]

#     elif numbers[i] > second_largest:
#         second_largest = numbers[i]

# print("Largest:", largest)
# print("Second Largest:", second_largest)