# takes a list
# returns a new list containing squares of the numbers

def sq_list(a):
    b = []
    for i in range(len(a)):
        a[i] = a[i]**2
        b.append(a[i])
    return b

numbers = [1,2,3,4,5]
print(f"Squared list is {sq_list(numbers)}")
