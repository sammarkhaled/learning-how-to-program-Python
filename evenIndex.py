#loop over given string and only print chars with an even index
def evenIndex():
    
    word = input("enter a word please: ")
    print(f"Original Word Is {word}")

    print( "Printing Only Even Indexes: ")

    for x in range(0, len(word), 2):
        print(word[x])
evenIndex()