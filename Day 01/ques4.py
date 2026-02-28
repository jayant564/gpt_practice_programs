# Write a program that:
# Takes marks (0–100)
# Prints grade:
# 90 and above → "A"
# 75–89 → "B"
# 50–74 → "C"
# Below 50 → "Fail"

marks = int(input("Enter your marks: "))

if marks<=100 and marks>=90:
    print("A")
elif marks>=75:
    print("B")
elif marks>=50:
    print("C")
else:
    print("Fail")
