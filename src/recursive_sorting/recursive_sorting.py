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

  arr1 = arr[:split]
  arr2 = arr[split:]  

  # TO-DO: Complete the helper function below to merge 2 sorted arrays
  
  return quick_sort(quick_sort(merge_sort(arr1)) + quick_sort(merge_sort(arr2)))

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
