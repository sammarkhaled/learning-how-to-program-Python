#get two integers from the user
#if their product <= 1000 ->multiplication
#else addition
def myfunc():
    
    number1 = int(input("first value : "))
    number2 = int(input("second value : "))

    if (number1 * number2 <= 1000):
        return "The result is", number1 * number2
    
    else:
        return "The result is", number1 + number2
print(myfunc())

#simple calculator
def addition(x, y):
    
    return x + y

def substraction(x, y):
    
    return x - y

def multiplication(x, y):
    
    return x * y

def division(x, y):
    
    return x / y

def calculator():
    
    after = 1

    while after == 1:
        x = int(input("choose the first number: "))
        y = int(input("choose the second number: "))
        choice = int(input("[1 = +] [2 = -] [3 = *] [4 = /]: "))

        if choice == 1:
            print(addition(x, y))

        elif choice == 2:
            print(substraction(x, y))

        elif choice == 3:
            print(multiplication(x, y))

        elif choice == 4:
            print(division(x, y))

        after = int(input("do you wish to continue?, [1 = yes] [2 = no]: "))
    print("byebye babes!")
calculator()