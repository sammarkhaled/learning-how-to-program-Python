#determines the maximum of the list
def maximum(array):
    
    x = array[0]

    for y in array:

        if y > x:
            x = y

    return x
print(maximum([1, 2, 5, 3]))

##determines the minimum of the list
def minimum(array):
    
    x = array[0]

    for y in array:

        if y < x:
            x = y

    return x
print(minimum([2, 7, 0, 11, 50]))

#sort array from big to small with the pre-defined max and min functions
def sortArray2(array):
    
    result = []
    y = maximum(array)
    z = minimum(array)

    for x in range(len(array) - 1):

        result.append(y)
        array.remove(y)
        y = maximum(array)

    result.append(z)
    return result
print(sortArray2([9, 2, 6, 18, 5]))