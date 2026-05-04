# Count Positives, Negatives, Zeros
# Input list → return:
# count of positive numbers
# count of negative numbers
# count of zeros

def countposneg(lst):
    p, n, z = 0, 0, 0
    for i in lst:
        if i==0:    z+=1
        elif i>0:    p+=1
        else:    n+=1
    print(f"Positive: {p}; Negative: {n}; Zeros: {z}")


#   Correct version

# def countposneg(lst):
#     p, n, z = 0, 0, 0
#     for i in lst:
#         if i == 0:
#             z += 1
#         elif i > 0:
#             p += 1
#         else:
#             n += 1
#     return p, n, z    
  
        
nums = [5, -2, 6, -3, 8, -9, 1, 7, 4, 0, -12, 5, 0, -5, 0, 6, 3]
countposneg(nums)
