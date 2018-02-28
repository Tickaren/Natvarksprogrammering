class Card:
    def __init__(self, suite, value):
        assert 1 <= suite <= 4 and 1 <= value <= 13
        self._suite = suite
        self._value = value
        # Skapar en dict med färgerna
        self._suite_dict = {
        1 : "Hjärter",
        2 : "Klöver",
        3 : "Spader",
        4 : "Ruter"
        }
        # Skapar en dict med alla värden:
        self._value_dict = {
        1 : "ess",
        2 : "två",
        3 : "tre",
        4 : "fyra",
        5 : "fem",
        6 : "sex",
        7 : "sju",
        8 : "åtta",
        9 : "nio",
        10 : "tio",
        11 : "knekt",
        12 : "dam",
        13 : "kung"
        }
    def getValue(self):
        return self._value
    def getSuite(self):
        return self.getSuite
    def __str__(self):
        return self._suite_dict[self._suite] + " " + self._value_dict[self._value]

from random import shuffle
class CardDeck:
    def __init__(self):
        self._cardsInDeck =[]
        self.reset()
    def shuffle(self):
        shuffle(self._cardsInDeck)
    def getCard(self):
        return self._cardsInDeck.pop()
    def size(self):
        return len(self._cardsInDeck)
    def reset(self):
        for s in range(1,5):
            for v in range(1,14):
                self._cardsInDeck.append(Card(s, v))

deck = CardDeck()
deck.shuffle()
while deck.size()>0:
    card = deck.getCard()
    print("Kortet {} har {}".format ( card, card.getValue()))
    
