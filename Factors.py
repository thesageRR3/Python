print("Today's goal is to factor numbers")
number = int(input("Enter a positive interger: "))

def factored(number):
    for n in range(1, number):
        factorial = number % n
        if factorial == 0:
            print(f"{n} is a factor of {number}")
    nextOrder = True
    while nextOrder:
        nextOrder = (input("hit \"A\" to go again or \"Q\" to quit: ")).lower()
        if nextOrder == "a":
            number = int(input("Enter a positive interger: "))
            factored(number)
        elif nextOrder == "q":
            nextOrder = False
            print("Thank you for using this program")
    return factored

factored(number)
