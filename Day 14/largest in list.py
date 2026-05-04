# Largest in List
# Find largest number in a list (NO max())

def largelist(n):
    lr = 0
    for i in n:
        if lr < i:
            lr = i
    return lr


#   Correct version

# def largelist(nums):
#     largest = nums[0]
#     for n in nums:
#         if n > largest:
#             largest = n
#     return largest


nums = [51, 21, 45, 82, 36, 55]
print(f"Largest ele in list: {largelist(nums)}")
