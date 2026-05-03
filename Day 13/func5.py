# Function to return maximum of two numbers

def maxtwo(a,b):
    if a>b: return a
    else:   return b

num1 = int(input("Enter num: "))
num2 = int(input("Enter num: "))
print(f"Max num among {num1} & {num2} is {maxtwo(num1, num2)}")
