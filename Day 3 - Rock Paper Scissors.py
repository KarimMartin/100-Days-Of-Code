import random  # Importing the random feature

game_is_on = True  # Setting the game state to true
computer_choices = ["rock", "paper", "scissors"]  # Listing the options for the computer
player_score = 0  # Initialising the player score
computer_score = 0  # Initialising the computer score


while game_is_on:  # While the game is active:
    computer_choice = random.choice(computer_choices)  # Computer selects rock, paper or scissors and stores in variable
    player_choice = input("Rock [r], Paper [p], Scissors [s]? ")  # Player selects rock, paper or scissors and stores in variable

    # Logic for the rock, paper, scissors game below:
    # If player wins, add one to player score.
    # If computer wins, add one to computer score.
    # If it's a draw, no one gets a score.
    if player_choice.upper() == "R" and computer_choice.upper() == "ROCK":
        print(f"I choose {computer_choice}. It's a draw.")
    elif player_choice.upper() == "R" and computer_choice.upper() == "SCISSORS":
        print(f"I choose {computer_choice}. You win!")
        player_score += 1
    elif player_choice.upper() == "R" and computer_choice.upper() == "PAPER":
        print(f"I choose {computer_choice}. You lose!")
        computer_score += 1
    elif player_choice.upper() == "S" and computer_choice.upper() == "ROCK":
        print(f"I choose {computer_choice}. You lose!")
        computer_score += 1
    elif player_choice.upper() == "S" and computer_choice.upper() == "SCISSORS":
        print(f"I choose {computer_choice}. It's a draw")
    elif player_choice.upper() == "S" and computer_choice.upper() == "PAPER":
        print(f"I choose {computer_choice}. You win!")
        player_score += 1
    elif player_choice.upper() == "P" and computer_choice.upper() == "ROCK":
        print(f"I choose {computer_choice}. You win!")
        player_score += 1
    elif player_choice.upper() == "P" and computer_choice.upper() == "SCISSORS":
        print(f"I choose {computer_choice}. You lose!")
        computer_score += 1
    elif player_choice.upper() == "P" and computer_choice.upper() == "PAPER":
        print(f"I choose {computer_choice}. It's a draw")
    else:
        print("I didn't get that. Please type r, s or p")

    play_again = input("Want to play again? [y] or [n] ")

    if play_again.upper() == "N":
        game_is_on = False
    elif play_again.upper() == "Y":
        game_is_on = True

print("Game over! Final score:")
print(f"Player {player_score} - {computer_score} Computer")
