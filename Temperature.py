print("This program converts temperatures between Farenheit & Celsius!")
print("You will be prompted to enter a temperature.")
print("Please enter it as \"degrees F\" or \"degrees C\"!")
print("Please include a space after the temperature!")
print("Eg: 98 F or 22 C!")

def heat_check():
    temperature = (input("Enter a temperature to convert: ")).lower()
    TEMP = temperature.replace(" ", "")
    if TEMP.endswith("f"):
        TEMP = float(TEMP.replace("f",""))
        def convert_far_to_cel(TEMP):
            C = (TEMP - 32) * 5/9
            return C
        C = convert_far_to_cel(TEMP)
        print(f"{TEMP:.2f}° F is {C:.2f}° C")

    elif TEMP.endswith("c"):
        TEMP = float(TEMP.replace("c",""))
        def convert_cel_to_far(TEMP):
            F = TEMP * 9/5 +32
            return F
        F = convert_cel_to_far(TEMP)
        print(f"{TEMP:.2f}° C is {F:.2f}° F")
    return heat_check

heat_check()

nextOrder = True

while nextOrder:
    nextOrder = (input("hit \"A\" to go again or \"Q\" to quit: ")).lower()
    if nextOrder == "a":
        heat_check()
    elif nextOrder == "q":
        nextOrder = False
        print("Thank you for using this program!")
