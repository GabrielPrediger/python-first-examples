userNameInput = input("Enter your name: ")

while True:
    try:
        print("*ONLY INTEGER NUMBERS*")
        userAgeInput = input("Enter your age: ")
        
        userAge = int(userAgeInput)
        break
    except:
        print("Please enter integers only.")