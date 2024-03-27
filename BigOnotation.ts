// Big O notation

// O(1) - Constant Time
// this code will always run in the same amount of time regardless of the size of the array
// because it only logs the first element of the array
// No 1.
function log(array: number[]) {
  console.log(array[0]);
  console.log(array[1]);
}

// No 2.
def contant_time_example(arr):
    return Array[0]

// O(n) - Linear Time
// this code will run in linear time because it will log each element of the array
// No 1.
function logAll(array: number[]) {
  for (let i = 0; i < array.length; i++) {
    console.log(array[i]);
  }
}

// No 2.
def linear_time_example(arr):
    for i in arr:
        print(i)
// O(n log n) - Linearithmic Time
// O(n^2) - Quadratic Time
// O(2^n) - Exponential Time
// O(n!) - Factorial Time

// Quadratic Time - O(n^2)
// this code will run in quadratic time because it has a nested loop
// No 1.
function addAndLog(array: number[]) {
  for (let i = 0; i < array.length; i++) {
    console.log(array[i]);
    for (let j = 0; j < array.length; j++) {
      console.log(array[i] + array[j]);
    }
  }
}
// No 2.
def quadratic_time_example(arr):
    for i in arr:
        print(i)
        for j in arr:
            print(i+j)

// Logarithmic Time - O(log n)
// this code will run in logarithmic time because it halves the input each time
// No 1.
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
// No 2.
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