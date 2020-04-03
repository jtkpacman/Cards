# Created by Jacob Kenyon. 3/30/2020

from random import shuffle


# The Card class defines what a card is.
# __init__ methods are similar to constructors in java.
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


# Lists containing suits and ranks.
suit = ['H', 'D', 'S', 'C']
rank = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K', 'A']


# The hand class defines the users hand.
class Hand:
    def __init__(self, cards, handSize):
        self.cards = cards
        self.handSize = handSize


# creates the deck and returns a list of cards.
def createDeck():
    deck = []
    deckSize = 0

    for i in range(len(suit)):
        for x in range(len(rank)):
            deck.append(Card(suit[i], rank[x]))
            deckSize += 1

    print("Created a deck of " + str(deckSize) + " cards.")
    return deck


# Shuffle the deck
def shuffleDeck(deck):
    shuffle(deck)
    print("Shuffled the deck.")


# Prints the current deck.
def showDeck(deck):
    for i in range(len(deck)):
        print("card", i + 1)
        print("The rank is: ", deck[i].rank, "\nThe suit is: ", deck[i].suit)


# Start the game operations.
# Assign the deck to a variable.
userDeck = createDeck()

# showDeck(userDeck)
shuffleDeck(userDeck)
# showDeck(userDeck)
