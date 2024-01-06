#check whether the first and last element are the same
def ListCompare(numbers_x):
    
    if (numbers_x[0] == numbers_x[-1]):
        return("Result Is True")
    
    else:
        return("Result Is False")
print(ListCompare([10, 20, 30, 40, 10]))
print(ListCompare([75, 65, 35, 75, 30]))

#print elements, if dividable by 5
def dividedByFive(mylist =[10, 20, 33, 46, 55]):
    
    for x in mylist: #for loops bei lists/arrays
        if not x % 5:
            print(x)
dividedByFive()

#print elements of a list individually
def test(listTest):
    
    x = 0
    while x < len(listTest):
        print(listTest[x])
        x = x + 1
test([1, 2, 3, 4, 5])

def test2(listTest2):
    
    x = len(listTest2) - 1
    while x >= 0:
        print(listTest2[x])
        x = x - 1
test2([1, 2, 3, 4, 5])

#two ways to reverse a list
def reverseList1(liste):
    
    liste.reverse()
    print(liste)
reverseList1([1, 2, 3, 4, 5])

#new list
def reverseList2(liste):
    
    sortedList = []

    for y in range(0, len(liste)):
        y = liste[-1]
        sortedList.append(liste[-1])
        liste.remove(liste[-1])

    return sortedList
print(reverseList2([11, 26, 3, 403, 50, 200]))