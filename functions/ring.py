import random 

coin = random.choice(["head", "tails", "straight"])

print(coin)

number = random.randint(1,10)
print(number)

cards = ["jack","king","queen"]
random.shuffle(cards)
for card in cards:
    print(card)



