def D6_roll():
    from random import randint
    if randint(1, 6) == 1:
        return "1"
    elif randint(1, 6) == 2:
        return "2"
    elif randint(1, 6) == 3:
        return "3"
    elif randint(1, 6) == 4:
        return "4"
    elif randint(1, 6) == 5:
        return "5"
    else:
        return "6"

num_rolls = int(input("Please input roll sample size: "))

tally1 = 0
tally2 = 0
tally3 = 0
tally4 = 0
tally5 = 0
tally6 = 0
total = 0

for trial in range(num_rolls):
    total = total + int(D6_roll())
    
    if D6_roll() == "1":
        tally1 = tally1 + 1

    elif D6_roll() == "2":
        tally2 = tally2 + 1

    elif D6_roll() == "3":
        tally3 = tally3 + 1

    elif D6_roll() == "4":
        tally4 = tally4 + 1
        
    elif D6_roll() == "5":
        tally5 = tally5 + 1
        
    else:
        tally6 = tally6 + 1

print(f"1 was rolled {tally1}x")
print(f"2 was rolled {tally2}x")
print(f"3 was rolled {tally3}x")
print(f"4 was rolled {tally4}x")
print(f"5 was rolled {tally5}x")
print(f"6 was rolled {tally6}x")

sum_of_rolls = (1 * tally1) + (2 * tally2) + (3 * tally3) + (4 * tally4) + (5 * tally5) + (6 * tally6)

print(total)
print(sum_of_rolls)
    
avg_roll_A = total / num_rolls
avg_roll_B = sum_of_rolls/ num_rolls
print(f"After roll x {num_rolls} of a D6, the average result was {avg_roll_A:.2f}, {avg_roll_B:.2f}")
