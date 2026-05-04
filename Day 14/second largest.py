# Find Second Largest
# From list, return second largest number

def second_largest(nums):
    largest = nums[0]
    second = None
    for n in nums:
        if n > largest:
            second = largest
            largest = n
        elif n != largest:
            if second is None or n > second:
                second = n
    return second