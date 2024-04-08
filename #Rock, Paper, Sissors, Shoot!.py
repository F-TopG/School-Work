#Rock, Paper, Sissors, Shoot!

import random

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (0 for Rock, 1 for Paper, 2 for Scissors, or any other key to exit): "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a number.")

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 0 and computer_choice == 2) or \
         (player_choice == 1 and computer_choice == 0) or \
         (player_choice == 2 and computer_choice == 1):
        return "You win!"
    else:
        raise ValueError("Computer wins!")

def print_choices(player_choice, computer_choice):
    choices = ["Rock", "Paper", "Scissors"]
    print(f"You chose {choices[player_choice]}. Computer chose {choices[computer_choice]}.")

def play_game():
    player_score = 0
    computer_score = 0

    while True:
        computer_choice = random.randint(0, 2)
        player_choice = get_user_choice()

        if player_choice not in [0, 1, 2]:
            print("Exiting the game. Final scores:")
            break

        try:
            result = determine_winner(player_choice, computer_choice)
            player_score += 1
            print(result)
        except ValueError as ve:
            computer_score += 1
            print(ve)

        print_choices(player_choice, computer_choice)
        print(f"Scores: Player {player_score} - {computer_score} Computer\n")

play_game()