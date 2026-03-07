# Write a function that:
# takes a list
# returns the count of even numbers

def count_even(a):
    count = 0
    for i in range(len(a)):
        if a[i] % 2 == 0:
            count += 1
    return count

numbers = [5,9,8,2,1,6,7,4,3,1,6,5,2,2,4,5,8]
print(f"Even elements in list is {count_even(numbers)}")
