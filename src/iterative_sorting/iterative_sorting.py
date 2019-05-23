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
  
  print(arr)

print('Insertion Sort My Solution')
insertion_sort([12, 11, 13, 5, 6])
insertion_sort([4, 3, 2, 10, 12, 1, 5, 6])

## Geeks for Geeks Solution of Insertion Sort

def insertion_sort_two(arr): 
  # Traverse through 1 to len(arr) 
  for i in range(1, len(arr)): 
    key = arr[i] 
    # Move elements of arr[0..i-1], that are 
    # greater than key, to one position ahead 
    # of their current position
    j = i-1
    
    while j >= 0 and key < arr[j]: 
      arr[j + 1] = arr[j] 
      j -= 1
    
    arr[j + 1] = key 
  
  print(arr)

print('Insertion Sort Second Geeks for Geeks Solution')
insertion_sort_two([12, 11, 13, 5, 6])
insertion_sort_two([4, 3, 2, 10, 12, 1, 5, 6])

### TO-DO: Complete the selection_sort() function below 

def selection_sort( arr ):
  # loop through n-1 elements

  for i in range(0, len(arr) - 1):
    cur_index = i
    smallest_index = cur_index
    # TO-DO: find next smallest element
    # (hint, can do in 3 loc) 
    
    # TO-DO: swap
  return arr


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
  
  print(arr)

print('Bubble Sort My Solution')
bubble_sort([12, 11, 13, 5, 6])
bubble_sort([4, 3, 2, 10, 12, 1, 5, 6])

## Geeks for Geeks Solution of Insertion Sort

def bubble_sort_two(arr): 
  n = len(arr) 
  
  # Traverse through all array elements 
  for i in range(n): 
    # Last i elements are already in place 
    for j in range(0, n-i-1): 
    # traverse the array from 0 to n-i-1
      # Swap if the element found is greater
      # than the next element 
      if arr[j] > arr[j+1] : 
        arr[j], arr[j+1] = arr[j+1], arr[j] 
  
  print(arr)

print('Bubble Sort Second Geeks for Geeks Solution')
bubble_sort_two([12, 11, 13, 5, 6])
bubble_sort_two([4, 3, 2, 10, 12, 1, 5, 6])

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
  return arr