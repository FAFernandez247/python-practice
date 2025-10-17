import random

roll_counter = 0
while True:
    roll = input("Roll the dice? (y/n): ")
    if roll.lower() == 'y':
        num_dice = int(input("How many dice do you want to roll? "))
        rolls = []
        for i in range(num_dice):
            dice = random.randint(1, 6)
            rolls.append(dice)
        print(f"🎲({", ".join(map(str, rolls))})🎲")
        roll_counter += 1
    elif roll.lower() == 'n':
        print(f"Thanks for playing! You rolled the dice {roll_counter} times.")
        break
    else:
        print("Invalid input.")
