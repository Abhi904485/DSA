# An efficient Python3 program to
# compute maximum sum of i * arr[i]


"""
so below is the approach 
deriving formula
arr[0]*0 + arr[1]*1 + arr[2]*2 = current_value 
arr[1]*0 + arr[2]*1 + arr[0]*2 = next_value
arr[1] + arr[2] + arr[2] = current_value
arr[2] + arr[0] + arr[0] + arr[2] +arr[1] = next_value + arr[2] +arr[1]
arr[1] + arr[2] + arr[2] + arr[0] +arr[0] = next_value + arr[2] +arr[1]
current_value + arr[0] +arr[0] =  next_value + arr[2] +arr[1]

********************************************************
current_value + 2*arr[0] - (arr[2]+arr[1]) =  next_value
********************************************************
"""


def maxSum(arr, n):
    all_element_sum = sum(arr)
    current_value_with_index_sum=0
    current_value_with_index_sum += sum([index * value for index, value in enumerate(arr)])
    res = 0
    for i in range(n):
        next_value_with_index_sum = current_value_with_index_sum - (all_element_sum-arr[i]) + arr[i]*(n-1)
        current_value_with_index_sum =  next_value_with_index_sum
        res =  max(res, current_value_with_index_sum)
    return res
    

        

arr = [8, 3, 1, 2]
n = len(arr)

print(maxSum(arr, n))
