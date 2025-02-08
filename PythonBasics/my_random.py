import random
number = random.randint(1, 6)


print(random.randint(1, 6))

low = 1
high = 20
options = ['Rock', 'Paper', 'Scissors']
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# generate between 0 to 1
number = random.random()*10
print(number)
number = random.randint(1, 6)
number = random.randint(low, high)
choice = random.choice(options)
print(choice)
random.shuffle(cards)
