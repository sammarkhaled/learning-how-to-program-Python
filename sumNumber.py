#ask the user for a number n and print the sum of the numbers 1 to n
# 1+2+3+(...)+n
# n+n-1+n-2+(...)+1
def sumNumber():
    
    numberN = int(input("n: "))

    Summe = 0

    for x in range(1, numberN+1):
        Summe = Summe + x

    return Summe
print(sumNumber())


def sumNumber2():

    numberN2 = int(input("n2: "))

    return sum(list(range(numberN2+1)))
print(sumNumber2())
