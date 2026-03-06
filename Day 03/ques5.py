# Takes 5 numbers
# Finds the average of the numbers
# (no sum() allowed)
# Formula
# average = total / count

nums = []

for a in range(5):
    b = int(input("Enter number: "))
    nums.append(b)

total = 0
count = 0

for a in range(len(nums)):
    total += nums[a]
    count += 1

print(f"Average = {total/count}")


# total = 0

# for num in nums:
#     total += num

# average = total / len(nums)

# print("Average =", average)
