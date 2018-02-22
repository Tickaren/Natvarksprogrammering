class CardDeck:
    def __init__(self):
        self.reset()
    def shuffle(self):
        pass
    def getCard(self):
        pass
    def size(self):
        pass
    def reset(self):
        for s in range(4):
            for v in range(13):
                self._cardsInDeck = Card(s + 1, v + 1)
        print(self._cardsInDeck)
