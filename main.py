from player import Player
from cards import Cards
from dealer import Dealer


#PLAY CANT STAND FIX IT


dealer1 = Dealer()
player1 = Player('Josh',1000)

deck1 = Cards()
deck1.shuffle()

while True:
    print()
    print(f"You have {player1.chips} chips")
    try:
        tempBet = int(input("Set Bet or Leave Black to Exit: "))
    except ValueError:
        break
    player1.setBet(tempBet)
    card = deck1.deck[0]
    player1.hitCard(card)
    deck1.hit()
    dCard = deck1.deck[0]
    dealer1.dealerHit(dCard)
    deck1.hit()
    card = deck1.deck[0]
    player1.hitCard(card)
    deck1.hit()
    dCard = deck1.deck[0]
    dealer1.dealerHit(dCard)
    deck1.hit()
    player1.setTotal()
    dealer1.setTotal()
    while True:
        if player1.hasBlackjack():
            break
        print()
        print(f"Dealer Upcard: {dealer1.hand[len(dealer1.hand)-1]}\nYour Hand: {player1.hand}")
        print()
        playerAction = input("To hit type 'h', to stand type 's': ")
        print()
        print(f"{'':{'-'}{'^'}{40}s}")
        if playerAction == 's':
            print()
            print(f"You have stood: {player1.hand}")
            player1.stand()
            break
        elif playerAction == 'h':
            card = deck1.deck[0]
            player1.hitCard(card)
            deck1.hit()
        player1.setTotal()
        if player1.bust():
            print()
            print(f"Your Hand: {player1.hand}, you have bust")
            break
        
    if player1.bust():
        print(f"You lost {player1.bet} chips.")
        player1.removeChips(player1.bet)
    else:
        if dealer1.hasBlackjack() and player1.hasBlackjack():
            print(f"Player Hand: {player1.hand}\nDealer Hand: {dealer1.hand}")
            print("Both have BLACKJACK")
        elif dealer1.hasBlackjack():
            print(f"Dealer BLACKJACK, you lost {player1.bet} chips.")
            player1.removeChips(player1.bet)
        elif player1.hasBlackjack():
            print(f"BLACKJACK, you hand is {player1.hand}\nYou Won {player1.bet*1.5} chips.")
            player1.addChips(player1.bet*1.5)
        else:
            while not(dealer1.stand()) and dealer1.handTotal < player1.handTotal:
                dCard = deck1.deck[0]
                dealer1.dealerHit(dCard)
                deck1.hit()
                dealer1.setTotal()

            if dealer1.bust():
                print(f"Dealer bust, you win {player1.bet} chips.")
                player1.addChips(player1.bet)
            elif dealer1.handTotal > player1.handTotal:
                print(f"Dealer had {dealer1.hand}\nYou lost {player1.bet} chips.")
                player1.removeChips(player1.bet)
            elif dealer1.handTotal == player1.handTotal:
                print(f"Dealer had {dealer1.hand}\nDRAW")
            elif dealer1.handTotal < player1.handTotal:
                print(f"Dealer had {dealer1.hand}\nYou won {player1.bet} chips.")
                player1.addChips(player1.bet)

    player1.reset()
    dealer1.reset()
    deck1.shuffle()