# Day 14 - Higher/Lower Game

import art
import game_data
import random

def pick_account():
  account = random.choice(game_data.data)
  return account

def play():
  # Set constants
  is_game_over = False
  score = 0

  # Pick random item from data list to be account A. Keep out of the loop, because account 2 will become account 1 everytime the user is right.
  account_1 = pick_account()

  print(art.logo)
  while not is_game_over:
    # Pick random item from data list to be B.
    account_2 = pick_account()
    
    # Prevent printing two same accounts 
    if account_1 == account_2:
      account_2 = pick_account()
    
    print(f"Compare A: {account_1['name']}, a {account_1['description']}, from {account_1['country']}.")
    print(art.vs)
    print(f"Against B: {account_2['name']}, a {account_2['description']}, from {account_2['country']}.")

    # Get input guess from user: Who has more followers? Type 'A' or 'B': 
    guess = input("Who has more followers? 'A' or 'B': ")

    # Check who has more followers and store the answer
    if account_1['follower_count'] > account_2['follower_count']:
      answer = "A"
    elif account_2['follower_count'] > account_1['follower_count']:
      answer = "B"

    # Compare the answer against the user guess and keep score.
    if guess == answer:
      score += 1
      print(f"You're right! Current score: {score}")
      account_1 = account_2
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      is_game_over = True
    

play()
    
