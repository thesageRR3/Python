print("This program converts temperatures between Farenheit & Celsius!")
print("You will be prompted to enter a temperature.")
print("Please enter it as \"degrees F\" or \"degrees C\"!")
print("Please include a space after the temperature!")
print("Eg: 98° F or 22° C or 295.15° K!")

def heat_check():
    temperature = (input("Enter a temperature to convert: ")).lower()
    TEMP = temperature.replace(" ", "")

    if TEMP.endswith("f"):
        unit = (input("Enter which scale (C or K) you wish to convert to: ")).lower()
        if unit == "c":
            TEMP = float(TEMP.replace("f",""))
            def convert_far_to_cel(TEMP):
                C = (TEMP - 32) * 5/9
                return C
            C = convert_far_to_cel(TEMP)
            print(f"{TEMP:.2f}° F is {C:.2f}° C")

        elif unit == "k":
            TEMP = float(TEMP.replace("f",""))
            def convert_far_to_kel(TEMP):
                K = ((TEMP - 32) * (5/9)) + 273.15
                return K
            K = convert_far_to_kel(TEMP)
            print(f"{TEMP:.2f}° F is {K:.2f}° K")
     
   
    elif TEMP.endswith("c"):
        unit = (input("Enter which scale (F or K) you wish to convert to: ")).lower()
        if unit == "f":
            TEMP = float(TEMP.replace("c",""))
            def convert_cel_to_far(TEMP):
                F = TEMP * 9/5 +32
                return F
            F = convert_cel_to_far(TEMP)
            print(f"{TEMP:.2f}° C is {F:.2f}° F")

        
        elif unit == "k":
            TEMP = float(TEMP.replace("c",""))
            def convert_cel_to_kel(TEMP):
                K = TEMP + 273.15
                return K
            K = convert_cel_to_kel(TEMP)
            print(f"{TEMP:.2f}° C is {K:.2f}° K")

        
    elif TEMP.endswith("k"):
        unit = (input("Enter which scale (F or C) you wish to convert to: ")).lower()
        if unit == "f":
            TEMP = float(TEMP.replace("k",""))
            def convert_kel_to_far(TEMP):
                F = ((TEMP - 273.15) * (9/5)) +32
                return F
            F = convert_kel_to_far(TEMP)
            print(f"{TEMP:.2f}° K is {F:.2f}° F")

            
        elif unit == "c":
            TEMP = float(TEMP.replace("k",""))
            def convert_kel_to_cel(TEMP):
                C = (TEMP - 273.15)
                return C
            C = convert_kel_to_cel(TEMP)
            print(f"{TEMP:.2f}° K is {C:.2f}° C")
 
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
