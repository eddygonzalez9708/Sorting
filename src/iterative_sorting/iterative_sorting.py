### TO-DO: Implement the Insertion Function below with your TA

## My Solution of Insertion Sort

def insertion_sort(arr):
  arr_len = len(arr)

  for x in range(1, arr_len):
    if (arr[x - 1] > arr[x]):
      arr[x - 1], arr[x] = arr[x], arr[x - 1]
  
      for y in range(x - 1, 0, -1):
        if (arr[y] < arr[y - 1]):
          arr[y], arr[y - 1] = arr[y - 1], arr[y]
        else:
          break
  
  return arr

print('Insertion Sort My Solution')
print(insertion_sort([12, 11, 13, 5, 6]))
print(insertion_sort([4, 3, 2, 10, 12, 1, 5, 6]))
print()

## Geeks for Geeks Solution of Insertion Sort

def insertion_sort_two(arr): 
  # Traverse through 1 to len(arr) 
  for i in range(1, len(arr)): 
    key = arr[i] 
    # Move elements of arr[0..i-1], that are 
    # greater than key, to one position ahead 
    # of their current position

    j = i - 1
    
    while j >= 0 and key < arr[j]: 
      arr[j + 1] = arr[j]
      j -= 1
    
    arr[j + 1] = key 
  
  return arr

print('Insertion Sort Second Geeks for Geeks Solution')
print(insertion_sort_two([12, 11, 13, 5, 6]))
print(insertion_sort_two([4, 3, 2, 10, 12, 1, 5, 6]))
print()

### TO-DO: Complete the selection_sort() function below 

def selection_sort(arr):
  # loop through n-1 elements

  for i in range(0, len(arr) - 1):
    cur_index = i
    smallest_index = cur_index

    for j in range(i + 1, len(arr)):
      # TO-DO: find next smallest element
      # (hint, can do in 3 loc) 
      if arr[j] < arr[smallest_index]:
        smallest_index = j
    
    # TO-DO: swap
    arr[smallest_index], arr[i] = arr[i], arr[smallest_index]

  return arr

print('Selection Sort My Solution')
print(selection_sort([12, 11, 13, 5, 6]))
print(selection_sort([4, 3, 2, 10, 12, 1, 5, 6]))
print()

### TO-DO: Implement the Bubble Sort function below

## My Solution of Bubble Sort

def bubble_sort(arr):
  passed = 0
  index = 0

  while passed < len(arr) - 1:
    if index == 0: 
      passed = 0

    if index < len(arr) - 1:
      if arr[index] > arr[index + 1]:
        arr[index], arr[index + 1] = arr[index + 1], arr[index]
        index += 1
      else: 
        index += 1
        passed += 1
    else:
      index = 0
  
  return arr

print('Bubble Sort My Solution')
print(bubble_sort([12, 11, 13, 5, 6]))
print(bubble_sort([4, 3, 2, 10, 12, 1, 5, 6]))
print()

## Geeks for Geeks Solution of Insertion Sort

def bubble_sort_two(arr): 
  n = len(arr) 
  
  # Traverse through all array elements 
  for i in range(n): 
    # Last i elements are already in place 
    for j in range(0, n - i - 1): 
    # traverse the array from 0 to n-i-1
      # Swap if the element found is greater
      # than the next element 
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j] 
  
  return arr

print('Bubble Sort Second Geeks for Geeks Solution')
print(bubble_sort_two([12, 11, 13, 5, 6]))
print(bubble_sort_two([4, 3, 2, 10, 12, 1, 5, 6]))
print()

# STRETCH: implement the Count Sort function below

def count_sort(arr):
  if len(arr) < 2:
    return arr

  # First Step - Find the min and max.

  minimum = min(arr)
  maximum = max(arr)

  if minimum < 0:
    return "Error, negative numbers not allowed in Count Sort"

  # Second Step - Create index from min to max

  # Third Step - Count the number of times each number appeared in the input 

  count = {num:0 for num in range(minimum, maximum + 1)}

  for item in arr:
    count[item] += 1
  
  # print(f'count 1 {count}')

  # Fourth Step - Create sumCount that will hold the sum of counts for the given index and the index to its left.

  for key in count:
    if key - 1 in count:
      count[key] += count[key - 1]
  
  # print(f'count 2 {count}')

  # Fifth Step - There are len(arr) numbers in the input so we will create len(arr) positions and fill those positions with the given numbers as per sumCount. After, reduce the val of the index in sumCount by 1 each time the number repeats in the input. 

  sorted_arr = [0 for x in range(len(arr))]
  
  # print(f'sorted arr 1 {sorted_arr}')

  for num in arr:
    val = count[num] - 1
    sorted_arr[val] = num
    count[num] -= 1
  
  # print(f'sorted arr 2 {sorted_arr}')

  return sorted_arr

print('Count Sort My Solution')
print(count_sort([12, 11, 13, 5, 6]))
print(count_sort([4, 3, 2, 10, 12, 1, 5, 6]))
print()