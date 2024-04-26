#  String Challenge
# Have the function StringChallenge(str) take the str parameter being passed and capitalize the first letter of each word. Words will be separated by only one space.

# Examples
# Input: "hello world"
# Output: Hello World
# Input: "i ran there"
# Output: I Ran There

def StringChallenge(strParam):
  # code goes here
  return ' '.join([i.capitalize() for i in strParam.split(' ')])
# keep this function call here
print(StringChallenge(raw_input()))

