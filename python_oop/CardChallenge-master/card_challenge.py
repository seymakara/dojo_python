from random import shuffle

class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def getValue(self):
        if (self.value == 1):
            return "Ace"
        elif (self.value == 11):
            return "Jack"
        elif (self.value == 12):
            return "Queen"
        elif (self.value == 13):
            return "King"
        else:
            return self.value

    def getSuit(self):
        if (self.suit == 1):
            return "Diamond"
        elif (self.suit == 2):
            return "Spade"
        elif (self.suit == 3):
            return "Clubs"
        else:
            return "Hearts"

class Deck(object):
    def __init__(self):
        val = 1
        suit = 1
        self.card_list = []
        for i in range(0, 52):
            self.card_list.append(Card(val, suit))
            if (val == 13):
                suit+= 1
                val = 1
            else:
                val+= 1
        self.discard = []

    def show(self):
        for i in self.card_list:
            print i.getValue(), i.getSuit()

    def show_discard(self):
        for i in self.discard:
            print i.getValue(), i.getSuit()

    def shuffle(self):
        shuffle(self.card_list)
 
    #shuffles discard pile back into deck, shuffle deck
    def reshuffle(self):
        for i in self.discard:
            self.card_list.append(i)
        shuffle(self.card_list)

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.card_list.pop()) #End of List is top of deck

    def deal(self, deck, num):
        for i in range(0, num):
            self.hand.append(deck.card_list.pop())

    def discard(self, deck):
        deck.discard.append(self.hand.pop()) #Front of List is bottom of deck


myDeck = Deck()
myDeck.show()
myDeck.shuffle()
myDeck.show()

me = Player("Jeff")
print len(myDeck.card_list)
me.draw(myDeck)
print len(myDeck.card_list)
me.discard(myDeck)
print len(myDeck.card_list)
myDeck.show_discard()

me.deal(myDeck, 5)
print len(myDeck.card_list)
