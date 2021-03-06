import collections

Card = collections.namedtuple("Card", ['rank', 'suit'])


class WodDeck:
    # suits = "heart, spade, club, diamond".split()
    # ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    # cards = ['heart_A', 'heart_2', 'heart_3', 'heart_4', 'heart_5', 'heart_6', 'heart_7',
    #          'heart_8', 'heart_9', 'heart_10', 'heart_J', 'heart_Q', 'heart_K',
    #
    #          'spade_A', 'spade_2', 'spade_3', 'spade_4', 'spade_5', 'spade_6', 'spade_7',
    #          'spade_8', 'spade_9', 'spade_10', 'spade_J', 'spade_Q', 'spade_K',
    #
    #          'club_A', 'club_2', 'club_3', 'club_4', 'club_5', 'club_6', 'club_7',
    #          'club_8', 'club_9', 'club_10', 'club_J', 'club_Q', 'club_K',
    #
    #          'diamond_A', 'diamond_2', 'diamond_3', 'diamond_4', 'diamond_5', 'diamond_6', 'diamond_7',
    #          'diamond_8', 'diamond_9', 'diamond_10', 'diamond_J', 'diamond_Q', 'diamond_K',
    #          ]
    # 动作
    flower = ['heart', 'spade', 'club', 'diamond']
    numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    # # 次数
    # number = ['6', '7', '8', '9', '10', 'J', 'Q', 'K']
    # bomb = ['A', '2', '3', '4', '5']
    # card = [flower, number]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]

    def remove(self, card):
        print("card", card)
        self.cards.remove(card)


class AthleteDeck:
    # suits = "heart, spade, club, diamond".split()
    # ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    athletes = ['heart_A', 'spade_A', 'club_A', 'diamond_A']

    def __len__(self):
        return len(self.athletes)

    def __getitem__(self, position):
        return self.athletes[position]

    def remove(self, card):
        print("card", card)
        print(self.athletes)
        self.athletes.remove(card)

    def init(self):
        athletes = ['heart_A', 'spade_A', 'club_A', 'diamond_A']
