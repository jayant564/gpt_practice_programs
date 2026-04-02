# Create this structure:
# students = [
#  {"name":"Alice","marks":85},
#  {"name":"Bob","marks":92},
#  {"name":"Charlie","marks":78}
# ]
# Write a loop that prints:
# Alice 85
# Bob 92
# Charlie 78

students = [
 {"name":"Alice","marks":85},
 {"name":"Bob","marks":92},
 {"name":"Charlie","marks":78}
]

for k in students:
    print(k["name"]["marks"])
