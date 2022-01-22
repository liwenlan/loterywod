import collections

Card = collections.namedtuple("Card", ['rank', 'suit'])

class FrenchDeck:
    suits = "heart, spade, club, diamond".split()
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")

    def __init__(self):
        self._cards = [Card(suit, rank) for rank in self.ranks
                       for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


