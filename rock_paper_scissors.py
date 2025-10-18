import random

choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
wins = 0
losses = 0

while True:
    user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()

    if user_choice not in choices:
        print("Invalid input.")
        continue

    computer_choice = random.choice(list(choices.values()))

    user_full_choice = choices[user_choice]

    print(f"You chose {user_full_choice}.")
    print(f"Computer chose {computer_choice}.")

    if user_full_choice == computer_choice:
        print(f"It's a tie!")
    elif (user_full_choice == 'rock' and computer_choice == 'scissors') or \
        (user_full_choice == 'scissors' and computer_choice == 'paper') or \
        (user_full_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
        wins += 1
    else:
        print("You lose!")
        losses += 1

    while True:
        play_again = input("Continue playing? (y/n): ").lower()
        if play_again == 'n':
            print(f"Final score - Wins: {wins}, Losses: {losses}")
            quit()
        elif play_again == 'y':
            break
        else:
            print("Invalid input")
