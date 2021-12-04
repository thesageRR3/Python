def D6_roll():
    from random import randint
    roll = randint(1, 6)
    return str(roll)

num_rolls = int(input("Please input roll sample size: "))

tally1 = 0
tally2 = 0
tally3 = 0
tally4 = 0
tally5 = 0
tally6 = 0
total = 0

for trial in range(num_rolls):
    roll = D6_roll()
    total += int(roll)

    if roll == "1":
        tally1 += 1

    elif roll == "2":
        tally2 += 1

    elif roll == "3":
        tally3 += 1

    elif roll == "4":
        tally4 += 1
        
    elif roll == "5":
        tally5 += 1
        
    else:
        tally6 += 1

print(f"1 was rolled {tally1}x")
print(f"2 was rolled {tally2}x")
print(f"3 was rolled {tally3}x")
print(f"4 was rolled {tally4}x")
print(f"5 was rolled {tally5}x")
print(f"6 was rolled {tally6}x")

sum_of_rolls = (tally1 + tally2 + tally3 + tally4 + tally5 + tally6)
avg_roll = round(total / num_rolls)

print(f"{sum_of_rolls} total rolls completed")
print(f"After roll x {num_rolls} of a D6, the average result was {avg_roll}")
