#functionality of a while loop
def lesson():
    
    x = 10

    while x > 0: #while loops more control
        x = x - 1
        print(x)
lesson()


def lesson2():
    
    x = 0
    while x < 3:
        x = x + 1
        print(x)
lesson2()

#request the number 5 from the user until typed in
def repeat():
    
    question = int(input("please type in the number 5: "))

    while question != 5:
        print("Nooo that's not 5")
        question = int(input("use your brain please... number 5: "))

    return("good job!!!")
print(repeat())