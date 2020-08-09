# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        # inner loop goes all the way to end
        for j in range(cur_index + 1, len(arr)):
            # print("i:",i,"j:", j,"====", arr) 
            if arr[smallest_index] > arr[j]:
                smallest_index = j
    
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
       
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
                swapped = True

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    if len(arr) == 0:
        return arr
    counts = [0] * (maximum + 1)
    
    for val in arr:
        counts[val] += 1

    for i in range(0, range(counts)):
        while counts[i] > 0:
            arr[j] = i
            j+=1
            counts[i] -= 1



    return arr

test_arr = [4,3,2,1]
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr2 = []
arr3 = [0, 1, 2, 3, 4, 5]

# selection_sort(arr1)
# selection_sort(arr2)
# selection_sort(arr3)
# selection_sort(test_arr)
bubble_sort(test_arr)
