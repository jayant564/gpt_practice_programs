# Count how many elements are greater than 10

nums = [2,5,8,69,5,6,12,7,8,36,1,12,15,8,59,64,24]
count = 0
for n in nums:
    if n > 10:
        count += 1
print(f"Ele greater than 10 is {count}")
