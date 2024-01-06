#find the first "*" after a sequence of "#", using binary search
def binarySearch(array):

    left = 0
    right = len(array) - 1
    result = - 1

    while (left <= right):
        middle = (left + right) // 2

        if (array[middle] == "*"):
            result = middle
            right = middle - 1

        else:
            left = middle + 1

    if (result != -1):
        print(f"first '*' at position {result} after '#' symbols.")
        
    else:
        print("'*' not found in list")

binarySearch(["#", "#", "#", "#", "#", "*", "*", "*", "*", "*", "*"])