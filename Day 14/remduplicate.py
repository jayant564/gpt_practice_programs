# Remove Duplicates
# Given list:[1,2,2,3,4,4,5]
# Return:[1,2,3,4,5]

def remove_duplicates(nums):
    result = []
    for n in nums:
        if n not in result:
            result.append(n)
    return result