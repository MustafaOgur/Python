import random
from art import logo, vs
from game_data import data
from replit import clear


def random_number():
    return random.randint(0,49)

print(logo)
game_score = 0
game_over = False


#A is first person , B is the second person.
A = data[random_number()]
    
while game_over == False:
    B = data[random_number()]
    
    if A == B:
        while A == B:
            B = data[random_number()]

    #Information of the data.
    name_A = A["name"]
    description_A = A["description"]
    country_A = A["country"]
    follower_A = A["follower_count"]
    
    name_B = B["name"]
    description_B = B["description"]
    country_B = B["country"]
    follower_B = B["follower_count"]

    print(f"Compare A: {name_A}, a {description_A}, from {country_A}.")
    print(vs)
    print(f"Against B: {name_B}, a {description_B}, from {country_B}.")

    #Ask user for a guess.
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    #Clear the screen between rounds.
    clear()
    print(logo)

    #Give user feedback on their guess.
    #Score keeping.
    if follower_A > follower_B and answer == "a":
        game_score += 1
        A = B
        print(f"You're right! Current score: {game_score}")
    elif follower_A < follower_B and answer == "b":
        game_score += 1
        A = B
        print(f"You're right! Current score: {game_score}")
    else:
        print(f"Sorry that's wrong. Final score: {game_score}")
        game_over = True


