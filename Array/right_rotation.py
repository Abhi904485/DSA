

def rotate_array(arr: list, n: int, k: int):
    arr = arr[k:n+1] + arr[0:k]
    return arr


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    n = len(arr)
    k = 8 % n
    if k <0:
        print(arr)
    else:
        print(rotate_array(arr=arr, n=n, k=k))
