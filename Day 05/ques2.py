# Write a program that:
# creates dictionary
# {"math":85, "physics":90, "chemistry":78}
# finds the average marks

marks = {"math":85, "physics":90, "chemistry":78}

total = 0
count = 0
for k in marks:
    total += marks[k]
    count += 1

print(f"Average is {total/count}")
