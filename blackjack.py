from platform import java_ver
import random


suits = ["Diamonds", "Spades", "Hearts", "Clubs"]

values = {2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 10:"Jack", 10:"Queen", 10:"King", 11:"Ace"}

ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]



class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"



class Deck():
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.all_cards.append(new_card)
    
    def shuffle(self):
        return random.shuffle(self.all_cards)
    
    def __str__(self):
        deck_comp = ''
        for card  in self.all_cards:
            deck_comp = deck_comp  + '\n '+ card.__str__()
        return deck_comp



        




new_deck = Deck()
new_deck.shuffle()



print(new_deck)
