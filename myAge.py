#calculate age based on birthmonth and year
import datetime
def myAge2():
    
    today = datetime.date.today()
    year = today.strftime("%Y")
    year = int(year)
    month = today.strftime("%m")
    month = int(month)
    birthYear2 = int(input("Insert your birth year : "))
    birthMonth = int(input("Insert your birth month : "))
    age = year - birthYear2

    if birthMonth > month:
        return f"You are {age - 1} years old in {year} !"
    
    else:
        return f"You are {age} years old in {year} !"
print(myAge2())

#calculate age based on your birthday, birthmonth and year(more accurate)
def myAge3():
    
    today = datetime.date.today()
    year = today.strftime("%Y")
    year = int(year)
    month = today.strftime("%m")
    month = int(month)
    day = today.strftime("%d")
    day = int(day)
    birthYear2 = int(input("Insert your birth year : "))
    birthMonth = int(input("Insert your birth month : "))
    birthDay = int(input("Insert your birth day : "))
    age = year - birthYear2

    if month < birthMonth or (month == birthMonth and day < birthDay):
        return f"You are {age - 1} years old in {year} !"
    
    else:
        return f"You are {age} years old in {year} !"
print(myAge3())