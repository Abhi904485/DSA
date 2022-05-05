from turtle import right


def binary_search(arr, start, end, element):
    while end >= start:
        mid = end - (end-start)//2
        if element == arr[mid]:
            return mid
        elif element < arr[mid]:
            end = mid - 1
        else:
            start = mid+1
    else:
        return False


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    start = 0
    end = len(arr)-1
    x = 10
    index = binary_search(arr, start, end, x)
    if index:
        print("Element is present at index {}".format(index))
    else:
        print("Element is not present")
