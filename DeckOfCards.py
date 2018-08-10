# This is an implementation of a deck of cards object. At any point, there are cards in the deck (in a certain order known only to the deck) and cards outside of the deck which are publicly known.
import random

# These are used to translate the values for the cards to something nice and printable
Valuereader = {1:'A', 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:'J', 12:'Q', 13:'K'}
Suitreader = {0:'♠', 1:'♥', 2:'♣', 3:'♦'}

# This is a single card, a card has a suit and a value. Suits can only be Hearts, Clubs, Spades or Diamonds and values range from 1 (Ace) to 13 (King).
class Card(object):
    Suit = ""
    Value = 0
    
    def __init__(self, suit, value):
        if (suit in range(4)) & (value in range(1,14)):
            self.Suit = suit
            self.Value = value
        else:
            raise ValueError("This is an invalid card!")
    
    def print(self):
        print(Suitreader[self.Suit], Valuereader[self.Value])

# A deck consists of (ordered) two arrays of cards. The first consists of the cards that are in the deck (secret to the outside world) and the second consists of the cards that are outside the deck (open to the world). In total there are always 52 cards and each combination of suit and value occurs precisely once.
class Deck(object):
    __In = []
    Out = []

    # Initialize a deck by putting 52 playing cards in a random order.
    def __init__(self):
        sorted_deck = []
        for suit in range(4):
            for value in range(1,14):
                sorted_deck.append(Card(suit, value))
        random.shuffle(sorted_deck)
        self.__In = sorted_deck
        self.Out = []
        
    # This function moves the top card from the (hidden) deck to the open cards stack.
    def draw_card(self):
        self.Out.append(self.__In[-1])
        del self.__In[-1]
    
    # This function prints either the (hidden) deck, or the cards that have been laid open, depending on whether inout is "in" or "out"
    def print(self, inout="in"):
        if inout == "in":
            for card in self.__In:
                card.print()
        elif inout == "out":
            for card in self.Out:
                card.print()
                
temp = Deck()