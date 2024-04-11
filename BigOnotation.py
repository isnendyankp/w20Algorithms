# // Big O notation

# // O(1) - Constant Time
# // this code will always run in the same amount of time regardless of the size of the array
# // because it only logs the first element of the array
# // No 1.
function log(array: number[]) {
  console.log(array[0]);
  console.log(array[1]);
}

# // No 2.
def constant_time_example(arr):
    return arr[0];

# // O(n) - Linear Time
# // this code will run in linear time because it will log each element of the array
# // No 1.
function logAll(array: number[]) {
  console.log(array[0]);
  console.log(array[1]);
  for (let i = 0; i < array.length; i++) {
    console.log(array[i]);
  }
}

# // No 2.
def linear_time_example(arr):
    for i in arr:
        print(i)


# // Quadratic Time - O(n^2)
# // this code will run in quadratic time because it has a nested loop
# // No 1.
function addAndLog(array: number[]) {
  for (let i = 0; i < array.length; i++) {
    console.log(array[i]);
    for (let j = 0; j < array.length; j++) {
      console.log(array[i] + array[j]);
    }
  }
}
# // No 2.
def quadratic_time_example(arr):
    for i in arr:
        print(i)
        for j in arr:
            print(i+j)

# // Logarithmic Time - O(log n)
# // this code will run in logarithmic time because it halves the input each time
# // No 1.
function binarySearch(array: number[], key: number) {
  let low = 0;
  let high = array.length - 1;
  let mid;
  let element;

  while (low <= high) {
    mid = Math.floor((low + high) / 2, 10);
    element = array[mid];
    if (element < key) {
      low = mid + 1;
    } else if (element > key) {
      high = mid - 1;
    } else {
      return mid;
    }
  }
  return -1;
}
# // No 2.
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1

# //  linearithmic time - O(n log n)
# //  this code will run in linearithmic time because it has a nested loop
# // No 1.
function sort(array: number[]) {
  if (array.length <= 1) {
    return array;
  }
  const middle = Math.floor(array.length / 2);
  const left = array.slice(0, middle);
  const right = array.slice(middle);

  return merge(sort(left), sort(right));
}

function merge(left: number[], right: number[]) {
  let result = [];
  let leftIndex = 0;
  let rightIndex = 0;

  while (leftIndex < left.length && rightIndex < right.length) {
    if (left[leftIndex] < right[rightIndex]) {
      result.push(left[leftIndex]);
      leftIndex++;
    } else {
      result.push(right[rightIndex]);
      rightIndex++;
    }
  }

  return result.concat(left.slice(leftIndex)).concat(right.slice(rightIndex));
}
# // No 2.
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    return result + left[left_index:] + right[right_index:]

# //  exponential time - O(2^n)
# //  this code will run in exponential time because it has a recursive function that calls itself twice
# // No 1.
function fibonacci(num: number) {
  if (num <= 1) {
    return num;
  }
  return fibonacci(num - 1) + fibonacci(num - 2);
}
# // No 2.
def exponential_time_example(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return exponential_time_example(n-1) + exponential_time_example(n-2)

# //  factorial time - O(n!)
# //  this code will run in factorial time because it has a recursive function that calls itself n times
# // No 1.
function factorial(num: number) {
  if (num <= 1) {
    return 1;
  }
  return num * factorial(num - 1);
}
# // No 2.
def factorial_time_example(n):
    if n == 0:
        return 1
    else:
        return n * factorial_time_example(n-1)
    
# //  cubic time - O(n^3)
# //  this code will run in cubic time because it has a nested loop that iterates over the array
# // No 1.
function cubicTime(array: number[]) {
  for (let i = 0; i < array.length; i++) {
    for (let j = 0; j < array.length; j++) {
      for (let k = 0; k < array.length; k++) {
        console.log(array[i] + array[j] + array[k]);
      }
    }
  }
}

# test cases cubic time
cubicTime([1, 2, 3, 4, 5])
cubicTime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# // No 2.
def cubic_time_example(arr):
    for i in arr:
        for j in arr:
            for k in arr:
                print(i+j+k)

# test cases cubic time
cubic_time_example([1, 2, 3, 4, 5])
cubic_time_example([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# //  factorial time - O(n!)
# //  this code will run in factorial time because it has a recursive function that calls itself n times
# // No 1.
function factorial(num: number) {
  if (num <= 1) {
    return 1;
  }
  return num * factorial(num - 1);
}

# // test cases factorial time
factorial(5)

# result: 120