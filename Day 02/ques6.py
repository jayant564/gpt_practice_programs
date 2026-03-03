# Find Maximum in List (Without max())

numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)
    
maximum = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] > maximum:
        maximum = numbers[i]

print("Max =", maximum)