# Given list:
# nums = [3,7,2,9,4,6]
# Create a new list containing only numbers greater than 5 using list comprehension.

nums = [3,7,2,9,4,6]

result = [x for x in nums if x>5]

print(result)
