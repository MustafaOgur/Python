import random
from replit import clear
from art import logo

#The number 11 in the list represents A. King,joker and queen are 10.
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
    return random.choice(cards)

def play_game():
    print(logo)
    
    user_cards=[]
    computer_cards=[]
    
    for number in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while sum(computer_cards) < 17:
        computer_cards.append(deal_card())
    
    print(f"   Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"   Computer's first card: {computer_cards[0]}\n")
    
    
    give_another = input("Type 'y' to get another card, type 'n' to pass: ")
    while give_another == "y":
        user_cards.append(deal_card())

        #A has two values. These are 1 and 11. When another card is requested, if the total of the cards is greater than 21, the A in the hand takes the value 1. In real life, too, the player chooses the value of A based on the sum of his cards.
        if 11 in user_cards and sum(user_cards) > 21:
            user_cards.remove(11)
            user_cards.append(1)
        
        print(f"   Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"   Computer's first card: {computer_cards[0]}\n")
            
        if sum(user_cards) > 21:
            print("You went over. You lose :( ")
            print(f"   Your final hand: {user_cards}, final score: {sum(user_cards)}")
            print(f"   Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}\n")               
            return
        give_another = input("Type 'y' to get another card, type 'n' to pass: ")

    
    if sum(user_cards) == sum(computer_cards):
        print("Draw :l")
    elif sum(computer_cards) == 21 and len(computer_cards) == 2:
        print("Lose, opponent has Blackjack ")
    elif sum(user_cards) == 21 and len(user_cards) == 2:
        print("Win with a Blackjack ")
    elif sum(computer_cards) > 21:
        print("Opponent went over. You win :) ")
    elif sum(user_cards) > sum(computer_cards):
        print("You win :) ")
    else:
        print("You lose :( ")

    print(f"   Your final hand: {user_cards}, final score: {sum(user_cards)}")
    print(f"   Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}\n")          



while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
