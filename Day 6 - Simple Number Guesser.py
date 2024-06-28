import random

game_is_on = True

user_score = 0
computer_score = 0

while game_is_on:

    max_value = int(input("What's the maximum number you want to guess up to? "))

    user_guess = int(input(f"You have chosen to guess between 0-{max_value}. Pick a number: "))
    computer_guess = random.randint(0, max_value)

    if user_guess == computer_guess:
        print(f"I guessed {computer_guess}. You win!")
        user_score = user_score + 1
        print("+1 point for you!")
    else:
        print(f"I guessed {computer_guess}. You lose!")
        computer_score = computer_score + 1
        print("+1 point for the computer.")

    play_again = input("Press enter to play again. Type 'Q' to quit: ")
    if play_again.upper() == "Q":
        game_is_on = False

print(f"Final score: User {user_score} - {computer_score} Computer")
