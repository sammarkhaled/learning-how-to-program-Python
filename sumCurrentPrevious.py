#count til 9, sum current number with previous number
def sumCurrentPrevious():
    
    previous = 0

    for c in range (10):
        print(f"Current Number {c} Previous Number {previous} Sum: {previous + c}")
        previous = c
sumCurrentPrevious()