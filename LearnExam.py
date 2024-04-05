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


