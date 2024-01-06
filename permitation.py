 #permitation
def permitation():

    a = int(input("a: "))
    b = int(input("b: "))
    c = a
    a = b
    b = c
    return f"b is {b}"
print(permitation())

#without using a third variable
def permitation2():
    
    a = 5
    b = 10
    a = a + b
    b = a - b
    a = a - b
    return f"a is {a}"
print(permitation2())