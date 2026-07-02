# Insertion Sort in monotonically decreasing order
def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i -1
        # move smaller values one position to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    numbers = [31, 41, 59, 30, 58, 22]
    
    print("Original array:", numbers)
    print("Sorted array in descending order:", insertion_sort_descending(numbers))
    
