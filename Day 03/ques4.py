# Takes 5 numbers
# Stores in list
# Creates a new list containing only numbers greater than 10

nums = []

for i in range(5):
    num = int(input("Enter number: "))
    nums.append(num)

nums2 = []

for i in range(len(nums)):
    if nums[i] > 10:
        nums2.append(nums[i])

print(nums2)
