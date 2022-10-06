# Recursive Binary Search algorithm in Python

def binarySearch(array, x, low, high):
    if high >= low:
        mid = low + (high - low)//2

        # If found at mid, then return the value

        if array[mid] == x:
            return mid
    
        # Search in  the first half
    
        elif array[mid] > x:
            return binarySearch(array, x, low, mid-1)
    
        # Search in the second half
    
        else:
            return binarySearch(array, x, mid + 1, high)

    # if not found then return -1
    else:
        return -1

# Example Array
 
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Enter element to search

x = int(input("Enter a number between 1 and 10 :: "))

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at position " + str(result))

else:
    print("Element not found !")