# Game class
    # set of cards
    # array of player objects in the game
    # a dealer: another player object
    # add player to player array function
    # random cards picker -> assign to player (drawCard function)
    # check win function
    
# player class
    # set of cards in hand
    # dictionary of card:value (maybe), or just integrate in handValue()
    # hand value calculator

class Player(object):
    def __init__(self, hand=[], bet=0, name=''):
        self.hand = hand
        self.handValue = self.handValue()
        self.bet = bet
        self.name = name

    def handValue(self):
        return 0

class BlackJack(object):
    def __init__(self, players=[]):
        self.deck = [] # add cards
        self.dealer = Player()
        self.players = players
        self.start()
    
    def start(self):
        # add cards to self.cards
        # give cards to dealer and players

    def drawCard(self):
        # give a random card from deck, remove it from deck

    def checkWin(self):
        # check if someone lost (hand value over 21)
            # remove from game if lost
        # check if everyone won: 
            # dealer goes over 21
        # check if one person won:
            # highest value under or equal to 21 among dealer and all players

    def anotherHand(self):
        # discard current cards
        # draw new cards
