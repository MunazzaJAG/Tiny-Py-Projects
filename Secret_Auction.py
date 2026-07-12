import art

yes_no= True

bidder={}

while yes_no:
    name= input("What is your name?")
    bid= int(input("What is your bid?: $"))
    yes_no= input("Are there any other bidder? Type 'yes' or 'no': ").lower()
    bidder[name]= bid
    print("\n"*20)
    if yes_no == "no":
        yes_no= False

highest_bid = max(bidder.values())
winner = max(bidder, key=bidder.get)

print(f"The winner is {winner} with a bid of ${highest_bid}")