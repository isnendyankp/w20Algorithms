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
    
# Binary Search
# This algorithm for searching an element in a list is efficient for large lists and is recommended for use in production code.
    
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1

# Test
arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

# Output
# Element found at index 3
    
# Interpolation Search
# This algorithm for searching an element in a list is efficient for large lists and is recommended for use in production code.
    
def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1

        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low]))

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# Test
arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
x = 18
result = interpolation_search(arr, x)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

# Output
# Element found at index 4

# Hash Table with hash map
# This algorithm for searching an element in a list is efficient for large lists and is recommended for use in production code.

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

# Test
t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 67
t["march 17"] = 63457
print(t["march 6"])

# Output
# 310

# Hash Table with hash map and collision handling
# This algorithm for searching an element in a list is efficient for large lists and is recommended for use in production code.

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

# Test
t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 67
t["march 17"] = 63457
print(t["march 6"])

# Output
# 310

