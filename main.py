import random
from art import logo
print(logo)
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card=random.choice(cards)
  return card
   
def calculate_score(cards):
  if sum(cards)==21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def compare(user_score,computer_score):
  if user_score==computer_score:
    return "draw"
  elif computer_score==0:
    return "You loose , computer has a blackjack"
  elif user_score==0:
    return "Win with blackjack "
  elif user_score>21:
    return "You went over , you loose"
  elif computer_score>21:
    return "computer went over , computer loose"  
  elif user_score>computer_score:
    return "you wins"
  else:
    return "computer wins"
def play_game():
  computer_cards = []  
  user_cards = []
  is_game_over=False
  for i in range(0,2):
    newcard=deal_card
    user_cards.append(newcard)
    computer_cards.append(newcard)
  
  while not is_game_over:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards) 
    print(f" Your cards: {user_cards}, current score {user_score}")
    print(f" Computer first choice {computer_cards[0]} ")
    if user_score==0 or computer_score==0 or user_score>21:
      is_game_over=True
    else:
      user_should_deal=input("type 'y' to get another card , type 'n' to pass ").lower()
      if user_should_deal=='y':
        user_cards.append(deal_card())
      else:
        is_game_over=True
  
  
  while computer_score!=0 and computer_score <17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)
  calculate_score()
  
  print(compare(user_score,computer_score))
from replit import clear 
while input("do you want to play the game of blackjack ? type 'y' or 'n':"):
  clear()
  play_game()