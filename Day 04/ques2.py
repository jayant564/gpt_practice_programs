# Write a function that:
# takes two numbers
# returns the larger number

def find_larg(a,b):
    if a>b: return a
    elif b>a: return b
    else: print("Both are equal")

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

result = find_larg(num1, num2)

print(f"{result} is the largest number")
