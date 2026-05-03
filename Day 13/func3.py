# Function to check if number is even (return True/False)

def check_evenodd(n):
    # if n % 2 == 0:  return True
    # else:   return False
    return n % 2 == 0

num = int(input("Enter num "))
print(check_evenodd(num))
