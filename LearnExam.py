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

# test the function
unsorted_list = [34, 27, 43, 3, 9, 82, 10]
print(merge_sort_desc(unsorted_list))  # [82, 43, 34, 27, 10, 9, 3] 
