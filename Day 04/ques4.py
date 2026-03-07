# Write a function that:
# takes a list
# returns the largest number

def larg_list(a):
    lrg = a[0]
    for i in range(1, len(a)):
        if a[i] > lrg:
            lrg = a[i]
    return lrg

nums = [5,8,6,3,9,7,5,1,2,4,8,9,2,4,5]

print(nums)
print(f"Largest ele of list: {larg_list(nums)}")