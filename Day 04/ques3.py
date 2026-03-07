# Write a function that:
# takes a list
# returns the sum of all elements

def sum_list(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum

nums = [5,8,6,3,9,7,5,1,2,4,8,9,2,4,5]

print(nums)
print(f"Sum of list elements: {sum_list(nums)}")
