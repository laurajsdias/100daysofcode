# Day 11 - Blackjack game

import random


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(your_score, computer_score):
    if your_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif your_score == 0:
        return "Win with a Blackjack"
    elif your_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif your_score > computer_score:
        return "You win!"
    else:
        return "You lose =/"

def play_game():
    your_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        your_cards.append(deal_card())
        computer_cards.append(deal_card())

    # While loop for the user
    while not is_game_over:
        your_score = calculate_score(your_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {your_cards}, current score: {your_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if your_score == 0 or computer_score == 0 or your_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                your_cards.append(deal_card()) 
            else:
                is_game_over = True

    # While loop for the computer
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {your_cards}, final score: {your_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(your_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()


### First take ###
# # pick 2 random cards for you
# # calculate the score (add the two random cards)
# human_first_card = random.choice(cards) 
# human_second_card = random.choice(cards)
# human_score = human_first_card + human_second_card

# # pick computer's first card
# computer_first_card = random.choice(cards)
# computer_second_card = random.choice(cards)
# computer_score = computer_first_card + computer_second_card

# if human_first_card == "11" and human_second_card == "10":
#     print("You win! BLACKJACK!")
# elif computer_first_card == "11" and computer_second_card == "10":
#     print("You lost. Computer's Blackjack!")

# # print first answers
# print(f"Your cards: [{human_first_card}, {human_second_card}], current score: {human_score}")
# print(f"Computer's first card: {computer_first_card}")

# should_continue = input("Type 'y' to get another card, type 'n' to pass: ")

# computer_cards = [computer_first_card]

# if should_continue == "y":
#     human_third_card = random.choice(cards)
#     human_score = human_first_card + human_second_card + human_third_card
#     print(f"Your cards: [{human_first_card}, {human_second_card}, {human_third_card}], current score: {human_score}")
#     print(f"Computer's first card: {computer_first_card}")






