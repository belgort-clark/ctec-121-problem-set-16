# Problem Set No. 16 - Problem 2

# STEP 1 - Your comments go here
import random


class CardDeck:
    # STEP 10 - Your comments go here
    deck = []
    # STEP 11 - Your comments go here

    def __init__(self):
        # STEP 12 - Your comments go here
        ranks = ['Ace', '2', '3', '4', '5', '6', '7',
                 '8', '9', '10', 'Jack', 'Queen', 'King']
        # STEP 13 - Your comments go here
        suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
        # STEP 14 - Your comments go here
        for suit in suits:
            # STEP 15 - Your comments go here
            for rank in ranks:
                # STEP 16 - Your comments go here
                self.deck.append([rank, suit])
        # STEP 17 - Your comments go here
        self.deck = self.deck

    # STEP 18 - Your comments go here
    def displayDeck(self):
        # STEP 19 - Your comments go here
        print("---Current Deck---")
        # STEP 20 - Your comments go here
        for card in self.deck:
            # STEP 21 - Your comments go here
            print(card[0], card[1])

    # STEP 22 - Your comments go here
    def dealCard(self):
        # STEP 23 - Your comments go here
        if len(self.deck) > 0:
            # STEP 24 - Your comments go here
            card = self.deck.pop()
            # STEP 25 - Your comments go here
            return card
        else:
            # STEP 26 - Your comments go here
            return "No cards to deal"

    # STEP 27 - Your comments go here
    def getDeckSize(self):
        # STEP 28 - Your comments go here
        deck = self.deck
        # STEP 29 - Your comments go here
        return len(deck)

    # STEP 30 - Your comments go here
    def shuffleDeck(self):
        # STEP 31 - Your comments go here
        random.shuffle(self.deck)


def main():
    # STEP 2 - Your comments go here
    deck1 = CardDeck()
    # STEP 3 - Your comments go here
    deck1.displayDeck()
    # STEP 4 - Your comments go here
    deck1.shuffleDeck()
    # STEP 5 - Your comments go here
    deck1.displayDeck()
    # STEP 6 - Your comments go here
    for i in range(52):
        # STEP 7 - Your comments go here
        card = deck1.dealCard()
        # STEP 8 - Your comments go here
        print(card[0], 'of', card[1])

    # STEP 9 - Your comments go here. Be sure to explain why the value 0 gets printed out.
    print(deck1.getDeckSize())


main()
