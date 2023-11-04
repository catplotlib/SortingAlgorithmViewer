from time import sleep

# Sorting Algorithms

# Bubble Sort
def bubble_sort(canvas, arr, draw_data, root, time_delay):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                draw_data(canvas, arr, [
                          'green' if x == j or x == j+1 else 'red' for x in range(len(arr))])
                root.update_idletasks()
                sleep(0.01)
    draw_data(canvas, arr, ['green' for x in range(len(arr))])

# Insertion Sort
def insertion_sort(canvas, arr, draw_data, root, time_delay):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = key
            draw_data(canvas, arr, ['green' if x == j or x ==
                      i else 'red' for x in range(len(arr))])
            root.update_idletasks()
            sleep(0.05)
    draw_data(canvas, arr, ['green' for x in range(len(arr))])

# Selection Sort
def selection_sort(canvas, arr, draw_data, root, time_delay):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw_data(canvas, arr, ['green' if x == i or x ==
                  min_idx else 'red' for x in range(len(arr))])
        root.update_idletasks()
        sleep(0.05)
    draw_data(canvas, arr, ['green' for x in range(len(arr))])

# Merge Sort
def merge_sort(canvas, arr, draw_data, root, time_delay):
    auxiliary_array = arr[:]
    merge_sort_algorithm(canvas, arr, 0, len(arr) - 1,
                         auxiliary_array, draw_data, root, time_delay)
    draw_data(canvas, arr, ['green' for x in range(len(arr))])


def merge_sort_algorithm(canvas, main_array, start, end, auxiliary_array, draw_data, root, time_delay):
    if start < end:
        middle = (start + end) // 2
        # Sort the first half
        merge_sort_algorithm(canvas, auxiliary_array, start,
                             middle, main_array, draw_data, root, time_delay)
        # Sort the second half
        merge_sort_algorithm(canvas, auxiliary_array,
                             middle + 1, end, main_array, draw_data, root, time_delay)
        # Merge the sorted halves
        do_merge(canvas, main_array, start, middle, end,
                 auxiliary_array, draw_data, root, time_delay)


def do_merge(canvas, main_array, start, middle, end, auxiliary_array, draw_data, root, time_delay):
    k = start
    i = start
    j = middle + 1
    while i <= middle and j <= end:
        if auxiliary_array[i] <= auxiliary_array[j]:
            main_array[k] = auxiliary_array[i]
            i += 1
        else:
            main_array[k] = auxiliary_array[j]
            j += 1
        k += 1
        draw_data(canvas, main_array, [
                  'green' if x == k else 'light green' if x < k else 'red' for x in range(len(main_array))])
        root.update_idletasks()
        sleep(time_delay)

    # Copy the remaining elements of the left half, if there are any
    while i <= middle:
        main_array[k] = auxiliary_array[i]
        i += 1
        k += 1
        draw_data(canvas, main_array, [
                  'green' if x == k else 'light green' if x < k else 'red' for x in range(len(main_array))])
        root.update_idletasks()
        sleep(time_delay)

    # Copy the remaining elements of the right half, if there are any
    while j <= end:
        main_array[k] = auxiliary_array[j]
        j += 1
        k += 1
        draw_data(canvas, main_array, [
                  'green' if x == k else 'light green' if x < k else 'red' for x in range(len(main_array))])
        root.update_idletasks()
        sleep(time_delay)

# Quick Sort
def quick_sort(canvas, arr, draw_data, time_delay, start, end):
    if start < end:
        pivot_index = partition(arr, start, end)
        quick_sort(canvas, arr, draw_data, time_delay, start, pivot_index-1)
        quick_sort(canvas, arr, draw_data, time_delay, pivot_index+1, end)
        
    draw_data(canvas, arr, ['green' if x <= end else 'red' for x in range(len(arr))])
    sleep(time_delay)


def partition(arr, start, end):
    pivot = arr[start]
    low = start + 1
    high = end

    while True:
        while low <= high and arr[high] >= pivot:
            high = high - 1
        while low <= high and arr[low] <= pivot:
            low = low + 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break

    arr[start], arr[high] = arr[high], arr[start]

    return high

# Heap Sort
def heapify(arr, n, i, canvas, draw_data, time_delay):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, canvas, draw_data, time_delay)

def heap_sort(canvas, arr, draw_data, time_delay):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i, canvas, draw_data, time_delay)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        draw_data(canvas, arr, ['green' if x > i else 'red' for x in range(len(arr))])
        sleep(time_delay)
        heapify(arr, i, 0, canvas, draw_data, time_delay)
    draw_data(canvas, arr, ['green' for _ in range(len(arr))])


# Counting Sort
def counting_sort(canvas, arr, draw_data, time_delay):
    max_val = max(arr)
    m = max_val + 1
    count = [0] * m                
    
    for a in arr:
        count[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            arr[i] = a
            draw_data(canvas, arr, ['green' if x <= i else 'red' for x in range(len(arr))])
            sleep(time_delay)
            i += 1
    draw_data(canvas, arr, ['green' for x in range(len(arr))])

    
# Bucket Sort
def insertion_sort_for_bucket(bucket):
    for i in range(1, len(bucket)):
        up = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > up:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = up
    return bucket

def bucket_sort(canvas, arr, draw_data, time_delay):
    max_val = max(arr)
    size = max_val // len(arr) + 1  # Ensure size is large enough to cover all elements
    buckets = [[] for _ in range(len(arr))]
    for i in range(len(arr)):
        j = min(int(arr[i] / size), len(arr) - 1)  # Ensure j is within the correct range
        buckets[j].append(arr[i])
    
    flat_list = []
    for i in range(len(buckets)):
        # Sort each bucket
        insertion_sort_for_bucket(buckets[i])
        flat_list.extend(buckets[i])
        # Draw the data after each bucket is sorted
        draw_data(canvas, flat_list + arr[len(flat_list):], ['green' if x < len(flat_list) else 'red' for x in range(len(arr))])
        sleep(time_delay)
    
    for i in range(len(arr)):
        arr[i] = flat_list[i]

    # Draw the final sorted array
    draw_data(canvas, arr, ['green' for _ in range(len(arr))])
