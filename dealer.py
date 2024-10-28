class Dealer:
    
    def __init__(self):
        self.hand = []
        self.handTotal = 0
        self.hasAce = False
    
    def dealerHit(self,card):
        self.hand.append(card)
    
    def setTotal(self):
        from cards import Cards
        tempTotal = 0
        for i in range(len(self.hand)):
            tempCard = self.hand[i]
            tempTotal += Cards.cardValue(tempCard)
        
        self.handTotal = tempTotal

    def stand(self):
        if self.handTotal >= 17:
            return True
        else:
            return False
    
    def bust(self):
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
    
    def reset(self):
        self.hand = []
        self.handTotal = 0
        self.hasAce = False
