# Learn Exam algorithm

# 1. isPalindrome
# Write a function that checks if a given string is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
# requirements
# 1. The function should be case-insensitive.(treat "Madam" and "madam" as the same word)
# 2. The function should ignore spaces and punctuation marks in the string.
# 3. Optimize your code for efficiency.


# Example
def is_palindrome(word):
    # Convert the word to lowercase
    word = word.lower()
    
    # Remove spaces and punctuation marks
    word = ''.join(e for e in word if e.isalnum())
    
    # Check if the word is a palindrome
    return word == word[::-1]

# Test true
word = "Madam"
print(is_palindrome(word))  # True

# Test false
word = "Hello"
print(is_palindrome(word))  # False

# Main Exam
def IsPalindrome(strParam):
    # convert the string to lowercase
    strParam = strParam.lower()

    # remove spaces and punctuation marks
    strParam = ''.join(e for e in strParam if e.isalnum())

    # check if the string is a palindrome
    return strParam == strParam[::-1]


  # code goes here
#   return strParam

# keep this function call here 
# print IsPalindrome(raw_input())






# 2. Merge Sort
#  implement the merge sort algorithm in python. Write a function that takes an unsorted list of integers as input and returns the list sorted in ascending order.

# Requirements
# 1. Your Function should implement the merge sort algorithm.
# 2. Optimize your code for efficiency.
# 3. Provide comments or explanations for any key steps or optimizations.

# Example
def merge_sort(arr):
    # Base case: If the array has less than 2 elements, return the array
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort the two halves
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Merge the sorted halves
    return merge(left, right)

# test the function
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(unsorted_list))  # [11, 12, 22, 25, 34, 64, 90]


#  Main exam Merge sort coderbyte

# Implement the merge sort algorithm in python. Write a function that takes an unsorted list of integers as input and returns the list sorted in ascending order.

# Requirements
# 1. Your Function should implement the merge sort algorithm.
# 2. Optimize your code for efficiency.
# 3. Provide comments or explanations for any key steps or optimizations.

# Example
Input: [38, 27, 43, 3, 9, 82, 10]
Output: [3, 9, 10, 27, 38, 43, 82]

Input: [5, 2, 8, 5, 9, 1, 5, 2]
Output: [1, 2, 2, 5, 5, 5, 8, 9]

def Mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = Mergesort(left)
    right = Mergesort(right)

    return merge(left, right)

    return arr

# keep this function call here
# print Mergesort(raw_input())



# 3. Merge Sort desc
# Implement the merge sort algorithm in python. Write a function that takes an unsorted list of integers as input and returns the list sorted in descending order.

# Requirements
# 1. Your Function should implement the merge sort algorithm.
# 2. Optimize your code for efficiency.
# 3. Provide comments or explanations for any key steps or optimizations.

# Example
def merge_sort_desc(arr):
    # Base case: If the array has less than 2 elements, return the array
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort the two halves
    left = merge_sort_desc(left)
    right = merge_sort_desc(right)
    
    # Merge the sorted halves in descending order
    return merge_desc(left, right)

def merge_desc(left, right):
    result = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Extend the result with the remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# test the function
unsorted_list = [34, 27, 43, 3, 9, 82, 10]
print(merge_sort_desc(unsorted_list))  # [82, 43, 34, 27, 10, 9, 3]

#  main assessment Merge sort desc coderbyte

# Implement the merge sort algorithm in python. Write a function that takes an unsorted list of integers as input and returns the list sorted in descending order.

# Requirements
# 1. Your Function should implement the merge sort algorithm.
# 2. Optimize your code for efficiency.
# 3. Provide comments or explanations for any key steps or optimizations.

# Examples
Input: [38, 27, 43, 3, 9, 82, 10]
Output: [82, 43, 38, 27, 10, 9, 3]

Input: [5, 2, 8, 5, 9, 1, 5, 2]
Output: [9, 8, 5, 5, 5, 2, 2, 1]

#  Base code:
def Mergesortdesc(arr):
    # if array has less than 2 elements
    if len(arr) <= 1:
        return arr

    # split array
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # recursively sort 
    left = Mergesortdesc(left)
    right = Mergesortdesc(right)

    return mergedesc(left, right)

def mergedesc(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # extend result with the remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result 

# keep this function call here 
print(Mergesortdesc(list(map(int, input().split()))))







# 4. Factorial Recursion
# Write a recursive function to calculate the factorial of a non-negative integer n. The factorial of  n is the product of all positive integers up to n.

# Requirements
# 1. Your function should use recursion to calculate the factorial.
# 2. Handle the base case appropriately.
# 3. Optimize your code for efficiency.
# 4. Provide comments or explanations for any key steps or optimizations.

# Example
def factorial_recursive(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    
    # Recursive case: n! = n * (n-1)!
    return n * factorial_recursive(n - 1)

# Test the function
n = 5
result = factorial_recursive(n)
print (result)  # 120





# 5. Binary Search Implementation
# Implement the binary search algorithm in python. Write a function that takes a sorted list of integers and a target value as input and returns the index of the target value if its present in the list, or -1 if target value is not found.

# Requirements
# 1. Your function should implement the binary search algorithm.
# 2. Handle the case whehre the list is empty.
# 3. Optimize your code for efficiency.
# 4. Provide comments or explanations for any key steps or optimizations.
# 5. Return the index of element.

# Example
def binary_search(arr, target) :
    # Check if the list is empty
    if not arr:
        return -1
    
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # If the target is found at mid, return the index
        if arr[mid] == target:
            return mid
        
        # If the target is greater than the mid element, ignore left half
        elif arr[mid] < target:
            low = mid + 1
        
        # If the target is smaller than the mid element, ignore right half
        else:
            high = mid - 1
    
    # If the target is not found in the list, return -1
    return -1

# Test the function
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

target_value = 7

result = binary_search(sorted_list, target_value)

print(result)  # 6