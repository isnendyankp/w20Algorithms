# Linear Search
# This algorithm for searching an element in a list is not efficient for large lists and is not recommended for use in production code.

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Test
arr = [64, 34, 25, 12, 22, 11, 90]
x = 22
result = linear_search(arr, x)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

# Output
# Element found at index 4

# Sentinel Linear Search
# This algorithm for searching an element in a list is not efficient for large lists and is not recommended for use in production code.
    
def sentinel_linear_search(arr, target):
    n = len(arr)
    
    # set the last element as the sentinel
    arr.append(target)

    i = 0
    while arr[i] != target:
        i += 1

    # remove the sentinel
    arr.pop()

    if i < n:
        return i # element found
    else:
        return -1 # element not found
    
# Test
arr = [64, 34, 25, 12, 22, 11, 90]
x = 22
result = sentinel_linear_search(arr, x)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

# Output
# Element found at index 4