# Game flow:
# Two entities involved: the player and the dealer
# Player and dealer will draw from a list of cards
# ---
# Dealer will present their cards, if they're over 21, player wins.
# Player will present their cards, if they're over 21, dealer wins.
# ---
# Dealers two cards will be added together and then displayed
# Players two cards will be added together and then displayed
# Player will be asked if he'd like to draw another card.
# ---
# If yes, draw another random card.
# Add card value to players total value
#   If player total value exceeds 21; player bust and dealer wins
#   If player total value = 21, player wins
# Otherwise, lock in players value.
# ---
# Once value locked in, dealer draws cards from list
# ---
# If dealer total > player total and < 21
#   Dealer wins
# If dealer total > 21
#   Player wins
# If dealer total = 21
#   Dealer wins



# Code that allows me to draw a random number from cards
import random


game_over = False  # Creating the game over state
while not game_over:

    def draw_card():
        new_card = random.choice(card_list)
        return new_card


    print("Welcome to Blackjack!")
    player_value = 0  # Card value for the player
    dealer_value = 0  # Card value for the dealer

    # List of cards that can be drawn
    card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    dealer_value = dealer_value + draw_card() + draw_card()  # Sets the initial value for the dealer
    player_value = player_value + draw_card() + draw_card()  # Sets the initial value for the player

    print(f"You have drawn {player_value}.")  # Telling the player what they've drawn.

    player_drawing_cards = False  # Setting the drawing state of the cards
    while player_drawing_cards != True:  # While the game state is set to false, do the below
        player_draw = input("Would you like to draw again (y) or (n)? ") # Ask if they'd like to draw another card.

        if player_draw.upper() == "N":  # If they say no:
            player_drawing_cards = True  # Stop the loop of drawing cards




        if player_draw.upper() == "Y":
            player_value = player_value + draw_card()
            print(f"You now have {player_value}.")
            if player_value == 21:
                print("Blackjack! You win!")
                player_drawing_cards = True
                game_over = True
            if player_value > 21:
                print("Bust! You lose!")
                player_drawing_cards = True
                game_over = True







print ("Thanks for playing")







