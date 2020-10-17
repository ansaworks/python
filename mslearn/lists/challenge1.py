import random

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
cards = []
selected_cards = []
i = 1

for suit in suits:
    for rank in ranks:
        cards.append(f'{rank} of {suit}')

print(f'There are {len(cards)} cards in the deck.')
print('Dealing ...')

while i <= 5 :
        i += 1
        selected_card = random.choice(cards)
        selected_cards.append(selected_card)
        cards.remove(selected_card)

print(f'There are {len(cards)} cards in the deck.')
print(f'Player has the following cards in their hand:\n {selected_cards}')
