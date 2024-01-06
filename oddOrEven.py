#check if number us odd or even
def oddOrEven():
    
    x = int(input("Give me a number to check if its odd or even"))

    if x % 2 == 0:
        return("The number is even!")
    
    else:
        return("The number is odd!")
    
print(oddOrEven())