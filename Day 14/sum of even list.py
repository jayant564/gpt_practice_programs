# Sum of Even Numbers
# Take a list and return sum of only even numbers

def eventotal(n):
# def sum_even(nums):       better func name
    total = 0
    for i in n:
        if i%2==0:  total+=i
    return total

nums = [5, 2, 6, 3, 8, 9, 1, 7, 4]
print(f"Total of even num in list: {eventotal(nums)}")
