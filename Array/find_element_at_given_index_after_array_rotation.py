'''
Input:
N = 5, X = 1, K = 2
Arr[] = {1, 2, 3, 4, 5}
Ranges[][] = {{0, 2}, {0, 3}}
Output: 3
Explanation: Rotating the elements in range 
0-2 and 0-3, we have array as 4 3 1 2 5. 
Element at first position is 3.
https://practice.geeksforgeeks.org/problems/find-the-element-at-given-index4630/1/
'''


def find_element(arr, ranges, k, index):
    for i in range(k-1, -1, -1):
        left = ranges[i][0]
        right = ranges[i][1]

        if index <= right and index >= left:
            if index == left:
                index = right
            else:
                index = index-1
    return arr[index]


if __name__ == "__main__":
    n = 5  # length of array
    index = 1  # element at index 1
    k = 2  # k circular rotation
    arr = [1, 2, 3, 4, 5]
    ranges = [[0, 2], [0, 3]]
    print(find_element(arr, ranges, k, index))


"""
 0 1 2 3 4                    
[1,2,3,4,5]
[2,3,1,4,5]   first rotation in range 0 to 2  here left = 0 right = 2
In Above 1 is at start so it went to 2nd index first rotation
In below 2 is at start so it will go to 2nd index second rotation
[3,1,2,4,5]   second rotation in range 0 to 2

so logic is if index in range so we need to take care otherwise no impact 
if index == left so after rotation it will move to right else index will move to left direction with index-1
l = 0
r = 2
index= 1
"""
