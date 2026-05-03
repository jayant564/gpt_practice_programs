# Function to take a list and return sum

def addlist(n):
    total = 0
    for i in n:
        total += i
    return total

nums = [1, 2, 3, 4, 5]
print(addlist(nums))
