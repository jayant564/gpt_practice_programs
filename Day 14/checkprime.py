# Check Prime Number
# Function that checks if number is prime

def checkprime(n):
    if n <= 1:
        return False
    for i in range(2, n):   #for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter: "))
print(f"{checkprime(num)}")
