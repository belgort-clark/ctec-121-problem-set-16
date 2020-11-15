# Problem Set No. 16 - Problem 1

def main():
    # STEP 9 - Your comments go here
    deck = create_deck()
    # STEP 10 - Your comments go here
    num_cards = int(input("How many cards should I deal? "))
    # STEP 11 - Your comments go here
    deal_cards(deck, num_cards)


def create_deck():
    # STEP 12 - Replace with your comments
    deck = {'Ace of Spades': 1, '2 of Spades': 2, '3 of Spades': 3, '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6, '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9, '10 of Spades': 10, 'Jack of Spades': 10, 'Queen of Spades': 10, 'King of Spades': 10,
            'Ace of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3, '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6, '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9, '10 of Hearts': 10, 'Jack of Hearts': 10, 'Queen of Hearts': 10, 'King of Hearts': 10}
    # STEP 13 - Replace with your comments
    return deck


def deal_cards(deck, number):
    # STEP 1 - Replace with your comments
    hand_value = 0
    # STEP 2 - Replace with your comments
    if number > len(deck):
        # STEP 3 - Replace with your comments
        number = len(deck)
    # STEP 4 - Replace with your comments
    for count in range(number):
        # STEP 5 - Replace with your comments
        card, value = deck.popitem()
        # STEP 6 - Replace with your comments
        print(card)
        # STEP 7 - Replace with your comments
        hand_value += value
    # STEP 8 - Replace with your comments
    print("Value of this hand:", hand_value)


main()
