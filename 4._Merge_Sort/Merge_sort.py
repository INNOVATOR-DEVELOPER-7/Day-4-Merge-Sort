# Function to merge two halves
def merge(arr, left, middle, right):
    # Create temporary arrays to hold the two halves
    n1 = middle - left + 1
    n2 = right - middle

    L = arr[left:middle + 1]
    R = arr[middle + 1:right + 1]

    # Merge the temporary arrays back into arr
    i = j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L, if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R, if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Function to perform Merge Sort
def merge_sort(arr, left, right):
    if left < right:
        middle = (left + right) // 2

        # Sort first and second halves
        merge_sort(arr, left, middle)
        merge_sort(arr, middle + 1, right)

        # Merge the sorted halves
        merge(arr, left, middle, right)

# Get the list of numbers from the user
user_input = input("Enter numbers separated by spaces: ")
# Convert the string input to a list of integers
arr = list(map(int, user_input.split()))

# Print the unsorted list
print("Unsorted list:", arr)
# Sort the list using Merge Sort
merge_sort(arr, 0, len(arr) - 1)
# Print the sorted list
print("Sorted list:", arr)
