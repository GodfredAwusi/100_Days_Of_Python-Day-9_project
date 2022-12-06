import os
from art import logo

# Console clearing function
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Logo
print(logo)
print("Welcome to the secret auction program.")

# Bidder dictionary
bidders = {}
# Other bidders option
others = False

# While loop to allow other bidders
while not others:
    # Bider in put
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: GHC "))
    # Parsing user input to the bidder dictionary
    bidders[name] = bid
    # Other bidders option
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if other_bidders == "yes":
        cls()
        print(logo)
        print("Welcome to the secret auction program.")
    elif other_bidders == "no":
        others = True
        cls()
        # Checking for winner
        highest_bid = 0
        winner = ""
        for bidder in bidders:
            if bidders[bidder] > highest_bid:
                highest_bid = bidders[bidder]
                winner = bidder
        print(f"The winner is {winner} with a bid of {highest_bid} ")



