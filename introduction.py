#ask for users name and age and greet the user
def introduction():
    
    name = input("name:")
    age = input("age:")

    return f"Hello {name}, u are {age} years old."
print(introduction())