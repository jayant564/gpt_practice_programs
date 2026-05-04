# Reverse List WITHOUT slicing
# You are NOT allowed to use [::-1]

def revlst(n):
    copylst = n.copy()
    copylst.reverse()
    return copylst

# def revlst(nums):
#     rev = []
#     for i in range(len(nums) - 1, -1, -1):
#         rev.append(nums[i])
#     return rev

nums = [5, 2, 6, 3, 8, 9, 1, 7, 4]
print(f"{revlst(nums)}")
