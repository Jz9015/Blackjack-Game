class Player:
    def __init__(self,name,chips):
        self.name = name
        self.chips = chips
        self.bet = 0
        self.hand = []
        self.handTotal = 0
        self.hasAce = False
        self.hasStood = False

    def setTotal(self):
        from cards import Cards
        tempTotal = 0
        for i in range(len(self.hand)):
            tempCard = self.hand[i]
            tempTotal += Cards.cardValue(tempCard)
        self.handTotal = tempTotal
    
    def stand(self):
        self.hasStood = True

    def bust(self):
        self.setTotal()
        if self.handTotal > 21 and 'A' in self.hand:
            self.handTotal -= 10
            self.hasAce = True
        if self.handTotal > 21:
            return True
        else:
            return False
    
    def hasBlackjack(self):
        self.setTotal()
        if self.handTotal == 21 and len(self.hand) == 2:
            return True
        else:
            return False
    
    def hitCard(self,card):
        self.hand.append(card)

    def setBet(self,pBet):
        self.bet = pBet
    
    def addChips(self,add):
        self.chips += add

    def removeChips(self,rev):
        self.chips -= rev
    
    def reset(self):
        self.hand = []
        self.handTotal = 0
        self.hasAce = False
        self.bet = 0
        self.hasStood = False