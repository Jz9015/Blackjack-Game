class Cards:

    baseDeck = ['A','A','A','A','K','K','K','K','Q','Q','Q','Q','J','J','J','J',
            '10','10','10','10','9','9','9','9','8','8','8','8','7','7','7',
            '7','6','6','6','6','5','5','5','5','4','4','4','4','3','3','3',
            '3','2','2','2','2']
    

    def __init__(self):
        self.deck = []
    
    def shuffle(self):
        import random
        tempDeck = ['','','','','','','','','','','','','','','','','','','','','','','','',
                    '','','','','','','','','','','','','','','','','','','','','','','','',
                    '','','','']
        indexes = []
        y = random.randint(0,51)
        for i in range(len(self.baseDeck)):
            while y in indexes:
                y = random.randint(0,51)
            indexes.append(y)
            tempDeck[i] = self.baseDeck[y]
        self.deck = tempDeck[:]

    def hit(self):
        self.deck.remove(self.deck[0])
    
    def cardValue(card):
        match card:
            case 'A':
                return 11
            case 'K':
                return 10
            case 'Q':
                return 10
            case 'J':
                return 10
            case '10':
                return 10
            case '9':
                return 9
            case '8':
                return 8
            case '7':
                return 7
            case '6':
                return 6
            case '5':
                return 5
            case '4':
                return 4
            case '3':
                return 3
            case '2':
                return 2
