# Function that:

# takes list
# returns count of even numbers

def count_even(n):
    count = 0 
    for i in n:
        if i%2==0:  count+=1
    return count

nums = [5, 5, 6, 2, 8, 3, 4, 7, 6, 1, 2, 21, 15, 68, 45]
print(f"Even num in list: {count_even(nums)}")
