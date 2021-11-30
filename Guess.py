print("I'm thinking of a number between 1 and 10")
print("Can you guess what the number is?")
guess = int(input("Please enter your guess: "))

counter = 0

def am_I_right(guess):
    if guess == 3:
        print("CONGRATULATIONS! How did you know?")
    elif (guess > 10):
        print("Remember we're guessing between 1  - 10")
    elif guess == 10:
        print("WRONG!")
    elif (guess == 2) or (guess == 4):
        print("You're really close!")
    else:
        print("That's not quite it, try again!")
    return am_I_right

am_I_right(guess)

while guess != 3:
    counter = counter +1
    if counter == 1:
        print(f"You have taken {counter} guess so far!")
    elif counter > 2:
        print("You're really not that good at this, huh?")
        print("Here's a hint, it comes after 2!")
    else:
        print(f"You have taken {counter} guesses so far!")     
    guess = int(input("Please enter your guess: "))
    am_I_right(guess) 
