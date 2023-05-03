from replit import clear
from art import logo
bids = {}

def bid_function(proposer,price):
   bids[proposer] = price
    
print(logo)
print("Welcome to the secret auction program.")

should_continue = True
while should_continue:    
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    
    bid_function(proposer=name,price=bid)
    clear()
    reply = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if reply == "no":
        should_continue = False
        clear()
    elif reply == "yes":
        clear()

max_bid = 0
winner = ""
for person in bids:
    if bids[person] > max_bid:
        max_bid = bids[person]
        winner = person
print(f"The winner is {winner} with a bid of ${max_bid}.")
    

