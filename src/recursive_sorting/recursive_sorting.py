import random

# TO-DO: Implement the quick_sort() function in the Guided Project with your TA

def quick_sort(arr):
  if len(arr) < 2:
    return arr

  pivot = 0
  ptr = len(arr) - 1
  direction = -1

  for x in range(0, len(arr)):
    if direction == -1 and arr[pivot] > arr[ptr]:
      arr[pivot], arr[ptr] = arr[ptr], arr[pivot]
      pivot, ptr = ptr, pivot
      direction = 1
    elif direction == 1 and arr[pivot] < arr[ptr]:
      arr[pivot], arr[ptr] = arr[ptr], arr[pivot]
      pivot, ptr = ptr, pivot
      direction = -1

    ptr += direction
    
  return quick_sort(arr[0:pivot]) + [arr[pivot]] + quick_sort(arr[pivot + 1:])

print('Quick Sort My Solution')
print(quick_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
print(quick_sort([]))
print(quick_sort([2]))
print(quick_sort([0, 1, 2, 3, 4, 5]))
print(quick_sort(random.sample(range(200), 10)))
print()

# TO-DO: Implement the Merge Sort function below USING RECURSION

def merge_sort(arr):
  if len(arr) < 2:
    return arr

  split = len(arr) // 2

  left = merge_sort(arr[:split])
  right = merge_sort(arr[split:])

  return merge(left, right) 

# TO-DO: Complete the helper function below to merge 2 sorted arrays
  
def merge(arr1, arr2):
  length = len(arr1) + len(arr2)
  merged_arr = [0] * length

  one = two = 0

  for x in range(length):
    if one >= len(arr1):
      merged_arr[x] = arr2[two]
      two += 1
    elif two >= len(arr2):
      merged_arr[x] = arr1[one]
      one += 1
    elif arr1[one] > arr2[two]:
      merged_arr[x] = arr2[two]
      two += 1
    else:
      merged_arr[x] = arr1[one]
      one += 1
  
  return merged_arr

print('Merge Sort My Solution')
print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
print(merge_sort([]))
print(merge_sort([2]))
print(merge_sort([0, 1, 2, 3, 4, 5]))
print(merge_sort(random.sample(range(200), 10)))
print()

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
