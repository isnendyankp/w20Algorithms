# Bubble sort algorithm
# This algorithm is not efficient for large lists and is not recommended for use in production code.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is:", arr)

# Output
# Sorted array is: [11, 12, 22, 25, 34, 64, 90]

# insertion sort
# this algorithm is efficient for small lists and is recommended for use in production code.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Test
arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
print("Sorted array is:", arr)

# Output
# Sorted array is: [11, 12, 22, 25, 34, 64, 90]

# selection sort
# this algorithm is not efficient for large lists and is not recommended for use in production code.
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Test
arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print("Sorted array is:", arr)

# Output
# Sorted array is: [11, 12, 22, 25, 34, 64, 90]

# merge sort
# this algorithm is efficient for large lists and is recommended for use in production code.
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Test
arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr)
print("Sorted array is:", arr)

# Output
# Sorted array is: [11, 12, 22, 25, 34, 64, 90]

# quick sort
# this algorithm is efficient for large lists and is recommended for use in production code.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Test
arr = [64, 34, 25, 12, 22, 11, 90]
arr = quick_sort(arr)
print("Sorted array is:", arr)

# Output
# Sorted array is: [11, 12, 22, 25, 34, 64, 90]