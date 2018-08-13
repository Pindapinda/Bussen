# This class simulates a game of Bussen.
from DeckOfCards import *
import time
suits =[0,1,2,3]
Suitreader = {0:'♠', 1:'♣', 2:'♦', 3:'♥'}

class Bussen(object):
    Deck = Deck()
    Phase = 0
    Phasecards =[[]]
    
    def __init__(self):
        self.Deck = Deck()
        self.Phase = 0
        self.Phasecards = [[]]
    
    # This function simulates the number of sips you have to take for guessing card colour (red or black). If the colour is guessed correctly, 0 is returned and otherwise 1 is returned. The input 0 corresponds to black and the input 1 corresponds to red.
    def guess_suit(self, guess):
        print(self.Phase)
        if self.Phase != 0:
            raise ValueError("guess_suit is being called in the wrong phase!")
        elif len(self.Phasecards[0])>3:
            raise ValueError("guess_suit is being called for what is at least the 5th time!")
        elif guess not in [0,1]:
            raise ValueError("invalid guess in guess_suit")
        else:
            drawn = self.Deck.draw_card()
            self.Phasecards[0].append(drawn)
            return(abs(int(drawn.Suit>1)-guess))
    
    # This function simulates the number of sips you have to take for guessing the difference between the drawn card and the card right above it. In this case 0 corresponds to guessing lower and 1 corresponds to higher.
    # TODO in bussen, guessing exact (so not higher or lower) is rewarded by allowing the player to force someone else to drink. This could be implemented in this algorithm as well.
    def guess_higherlower(self, guess):
        if self.Phase != 1:
            raise ValueError("guess_higherlower is being called in the wrong phase!")
        elif len(self.Phasecards[1])>3:
            raise ValueError("guess_higherlower is being called for what is at least the 5th time!")
        elif guess not in [0,1]:
            raise ValueError("invalid guess in guess_higherlower")
        else:
            drawn = self.Deck.draw_card()
            self.Phasecards[1].append(drawn)
        if guess==0:
            return 1-int(drawn.Value <= self.Phasecards[0][len(self.Phasecards[1])-1].Value)
        else:
            print('here', self.Phasecards[0][len(self.Phasecards[1])-1].Value)
            return 1-int(drawn.Value >= self.Phasecards[0][len(self.Phasecards[1])-1].Value)
    
    # This function simulates guessing whether the drawn card will have a value that is in the range between the two cards above it or outside of it. In this case 0 corresponds to guessing inside and 1 corresponds to outside.
    # TODO in bussen, guessing exact (so not in between or outside) is rewarded by allowing the player to force someone else to drink. This could be implemented in this algorithm as well.
    def guess_inout(self, guess):
        if self.Phase != 2:
            raise ValueError("guess_inout is being called in the wrong phase!")
        elif len(self.Phasecards[2])>3:
            raise ValueError("guess_inout is being called for what is at least the 5th time!")
        elif guess not in [0,1]:
            raise ValueError("invalid guess in guess_inout")
        else:
            drawn = self.Deck.draw_card()
            self.Phasecards[2].append(drawn)
            minval = min(self.Phasecards[0][len(self.Phasecards[2])-1].Value, self.Phasecards[1][len(self.Phasecards[2])-1].Value)
            maxval = max(self.Phasecards[0][len(self.Phasecards[2])-1].Value, self.Phasecards[1][len(self.Phasecards[2])-1].Value)
        if guess==0:
            return 1-((drawn.Value >= minval) & (drawn.Value <= maxval))
        else:
            return 1-((drawn.Value <= minval) | (drawn.Value >= maxval))
            
    # This function simulates guessing whether the suit of the drawn card is already represented in the three cards above it or not. In this case 0 corresponds to guessing already represented and 1 corresponds to guessing it is not represented yet.
    def guess_suit2(self, guess):
        if self.Phase != 3:
            raise ValueError("guess_suit2 is being called in the wrong phase!")
        elif len(self.Phasecards[3])>3:
            raise ValueError("guess_suit2 is being called for what is at least the 5th time!")
        elif guess not in [0,1]:
            raise ValueError("invalid guess in guess_suit2")
        else:
            drawn = self.Deck.draw_card()
            self.Phasecards[3].append(drawn)
            shown = [self.Phasecards[0][len(self.Phasecards[3])-1].Suit, self.Phasecards[0][len(self.Phasecards[1])-1].Suit, self.Phasecards[0][len(self.Phasecards[2])-1].Suit]
            if guess == 0:
                return int(drawn.Suit not in shown)
            else:
                return int(drawn.Suit in shown)
                
    def bussen(self):
        print("Welcome to bussen v0.1! \nThis is made possible by a drunk Stefan.")
        input("Press enter to continue \n")
        guess = input("For the first phase, please guess a card colour, type 0 + enter to guess 'black' and 1 + enter to guess 'red'.  ")
        error = self.guess_suit(int(guess))
        print("The drawn card is:")
        self.Phasecards[0][-1].print()
        print("Your error is: ", error)
        
        for i in range(1,4):
            guess = input("Please guess colour again, type 0 + enter to guess 'black' and 1 + enter to gess 'red'.  ")
            error += self.guess_suit(int(guess))
            print("The drawn card is:")
            self.Phasecards[0][-1].print()
            print("Your cumulative error is: ", error)
            time.sleep(0.2)
            
        self.Phase = 1
        self.Phasecards.append([])
        time.sleep(1.5)
        
        print("\nFor the second phase, please guess whether the card is lower or higher than the last one: ")
        self.Phasecards[0][0].print()
        guess = input("Please type 0 + enter to guess lower and 1 + enter to guess higher: ")
        error += self.guess_higherlower(int(guess))
        print("The drawn card is: ")
        self.Phasecards[1][-1].print()
        print("Your cumulative error is: ", error)
        
        for i in range(1,4):
            print("Please guess again whether the card is lower or higher than the last one: ")
            self.Phasecards[0][i].print()
            guess = input("Please type 0 + enter to guess lower and 1 + enter to guess higher: ")
            error += self.guess_higherlower(int(guess))
            print("The drawn card is: ")
            self.Phasecards[1][-1].print()
            print("Your cumulative error is: ", error)
            time.sleep(0.2)
        
        self.Phase = 2
        self.Phasecards.append([])
        time.sleep(1.5)
        
        print("\nFor the third phase, please guess whether the card will be between the values of the last two or outside of it: ")
        self.Phasecards[0][0].print()
        self.Phasecards[1][0].print()
        guess = input("Please type 0 + enter to guess between and 1 + enter to guess outside: ")
        error += self.guess_inout(int(guess))
        print("The drawn card is: ")
        self.Phasecards[2][-1].print()
        print("Your cumulative error is: ", error)
        
        for i in range(1,4):
            print("Please guess again whether the card will be inside or outside the last two cards: ")
            self.Phasecards[0][i].print()
            self.Phasecards[1][i].print()
            guess = input("Please type 0 + enter to guess between and 1 + enter to guess outside: ")
            error += self.guess_inout(int(guess))
            print("The drawn card is: ")
            self.Phasecards[2][-1].print()
            print("Your cumulative error is: ", error)
            time.sleep(0.2)
            
        self.Phase = 3
        self.Phasecards.append([])
        time.sleep(1)
            
        print("\n For the fourth and final phase, please guess whether the suit of the card has already been drawn above: ")
        print(Suitreader[self.Phasecards[0][0].Suit], Suitreader[self.Phasecards[1][0].Suit], Suitreader[self.Phasecards[2][0].Suit])
        guess = input("Please type 0 + enter to guess already represented and 1 + enter to guess not yet represented: ")
        error += self.guess_suit2(int(guess))
        print("The drawn card is: ")
        self.Phasecards[3][-1].print()
        print("Your cumulative error is: ", error)
        
        for i in range(1,4):
            print("Please guess again whether the suit of the card has already been drawn above: ")
            print(Suitreader[self.Phasecards[0][0].Suit], Suitreader[self.Phasecards[1][0].Suit], Suitreader[self.Phasecards[2][0].Suit])
            guess = input("Please type 0 + enter to guess already represented and 1 + enter to guess not yet represented: ")
            error += self.guess_suit2(int(guess))
            print("The drawn card is: ")
            self.Phasecards[3][-1].print()
            print("Your cumulative error is: ", error)
        
        print("Thank you for playing!")
        
buske = Bussen()
buske.bussen()
    
