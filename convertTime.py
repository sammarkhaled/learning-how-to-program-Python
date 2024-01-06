#Evaluate whether the given year is a leap year or not
def leapYear(year1):
    
    if year1 %10 == 0 and year1 %400 == 0:
        return True
    
    elif year1 %4 == 0:
        return True
    
    else:
        return False
print(leapYear(year1 = int(input("year : "))))

#convert seconds into minutes
#warning, if the amount of seconds does not reach a minute yet
def secondMin(seconds):
    
    minutes = int(seconds / 60)
    if seconds < 60:
        return "The number of seconds doesn't reach a full minute yet:("
    
    else:
        return f"The amount of mins is {minutes}:{seconds % 60}"
print(secondMin(int(input("sec to convert: "))))