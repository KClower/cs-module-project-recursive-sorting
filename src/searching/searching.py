# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if start > end:
        return -1

    middle = (start + end) // 2

    if arr[middle] == target:
        return middle
    elif arr[middle] > target:
        return binary_search(arr, target, start, middle - 1)
    else:
        return binary_search(arr, target, middle + 1, end)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    start = 0
    end = len(arr) - 1

    is_ascending = arr[start] < arr[end]

    while start <= end:
        middle = (start + end) // 2

        if arr[middle] == target:
            return middle
        
        if is_ascending:
            if target < arr[middle]:
                end = middle - 1
            else:
                start = middle + 1
        else:
            if target > arr[middle]:
                end = middle - 1
            else:
                start = middle + 1
    return -1
