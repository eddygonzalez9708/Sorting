### TO-DO: Implement the Insertion Function below with your TA

# My Solution of Insertion Sort

def insertionSort(arr):
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

insertionSort([12, 11, 13, 5, 6])
insertionSort([4, 3, 2, 10, 12, 1, 5, 6])

# Geeks for Geeks Solution of Insertion Sort

def insertionSortTwo(arr): 
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

insertionSortTwo([12, 11, 13, 5, 6])
insertionSortTwo([4, 3, 2, 10, 12, 1, 5, 6])

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr