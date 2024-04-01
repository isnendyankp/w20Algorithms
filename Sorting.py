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

# heap sort
# this algorithm is efficient for large lists and is recommended for use in production code.
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# Test
arr = [64, 34, 25, 12, 22, 11, 90]
heap_sort(arr)
print("Sorted array is:", arr)

# Output
# Sorted array is: [11, 12, 22, 25, 34, 64, 90]

# Comparison of sorting algorithms
# Bubble sort
# Time complexity: O(n^2)
# Space complexity: O(1)
# Insertion sort
# Time complexity: O(n^2)
# Space complexity: O(1)
# Selection sort
# Time complexity: O(n^2)
# Space complexity: O(1)
# Merge sort
# Time complexity: O(n log n)
# Space complexity: O(n)
# Quick sort
# Time complexity: O(n log n)
# Space complexity: O(log n)
# Heap sort
# Time complexity: O(n log n)

# The best sorting algorithm to use depends on the size of the list and the specific requirements of the application. For small lists, insertion sort is a good choice. For large lists, merge sort or quick sort are recommended. Heap sort is also a good choice for large lists, as it has a time complexity of O(n log n) and is an in-place sorting algorithm. Bubble sort and selection sort are not recommended for use in production code, as they have a time complexity of O(n^2) and are not efficient for large lists.
