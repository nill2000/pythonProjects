import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        # same as - return self.rank["rank"] + " of " + self.suit
        return f"{self.rank['rank']} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        ranks = [
            {"rank": "A", "value": 11}, 
            {"rank": "2", "value": 2}, 
            {"rank": "3", "value": 3}, 
            {"rank": "4", "value": 4}, 
            {"rank": "5", "value": 5}, 
            {"rank": "6", "value": 6}, 
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8}, 
            {"rank": "9", "value": 9}, 
            {"rank": "10", "value": 10}, 
            {"rank": "J", "value": 10}, 
            {"rank": "Q", "value": 10}, 
            {"rank": "K", "value": 10}
        ]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffleCards(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)
        

    def dealCards(self, amount):
        cardsDealt = []
        for num in range(amount):
            if len(self.cards) > 0:
                num = self.cards.pop()
                cardsDealt.append(num)
        return cardsDealt

class Hand:
    def __init__(self, dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def addCard(self, cardList):
        self.cards.extend(cardList)

    def calculateValue(self):
        self.value = 0
        hasAce = False
        
        for card in self.cards:
            cardValue = int(card.rank["value"])
            self.value += cardValue
            if card.rank["rank"] == "A":
                hasAce = True
        
        if hasAce and self.value > 21:
            self.value -= 10

    def getValue(self):
        self.calculateValue()
        return self.value

    def isBlackjack(self):
        return self.getValue() == 21

    def display(self, showDealerCards=False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand''')
        
        for index, card in enumerate (self.cards):
            
            if index == 0 and self.dealer and not showDealerCards and not self.isBlackjack():
                print("hidden")
            else:
                print(card)

        if not self.dealer:
            print("Value:", self.getValue())
        print()

class Game:
    def play(self):
        gameNumber = 0
        gamesToPlay = 0
        while gamesToPlay <= 0:
            try:
                gamesToPlay = int(input("How many games?: "))
            except:
                print("Enter a number greater than 0")

        while gameNumber < gamesToPlay:
            gameNumber += 1
            deck = Deck()
            deck.shuffleCards()
            playerHand = Hand()
            dealerHand = Hand(dealer=True)
            for i in range(2):
                playerHand.addCard(deck.dealCards(1))
                dealerHand.addCard(deck.dealCards(1))

            print()
            print("*" * 30) 
            print(f"Game {gameNumber} of {gamesToPlay}")
            print("*" * 30) 
            playerHand.display()
            dealerHand.display()
            
            if self.checkWinner(playerHand, dealerHand):
                continue
            
            choice = ""
            while playerHand.getValue() < 21 and choice not in ["stand"]:
                choice = input("Hit or Stand: ").lower()
                
                print()
                
                while choice not in ["hit", "stand"]:
                    choice = input("Choose specifically hit or stand ").lower()
                    print()
                
                if choice in ["hit"]:
                    playerHand.addCard(deck.dealCards(1))
                    playerHand.display()
                
            if self.checkWinner(playerHand, dealerHand):
                continue

            playerHandValue = playerHand.getValue()
            dealerHandValue = dealerHand.getValue()
            
            while dealerHandValue < 17:
                dealerHand.addCard(deck.dealCards(1))
                dealerHandValue = dealerHand.getValue()
            dealerHand.display(showDealerCards=True)

            if self.checkWinner(playerHand, dealerHand):
                continue

            print("Final Reseults")
            print("Your Hand: ", playerHandValue)
            print("Dealer's Hand: ", dealerHandValue)

            self.checkWinner(playerHand, dealerHand, True)

        print("Game Ended")

    
    def checkWinner(self, playerHand, dealerHand, gameOver=False):
        if not gameOver:
            if playerHand.getValue() > 21:
                print("Dealer Wins")
                return True
            elif dealerHand.getValue() > 21:
                print("Player Wins")
                return True
            elif playerHand.isBlackjack() and dealerHand.isBlackjack():
                print("Tie")
            elif playerHand.isBlackjack():
                print("You Win")
                return True
            elif dealerHand.isBlackjack():
                print("Dealer Wins")
        else:
            if playerHand.getValue() > dealerHand.getValue():
                print("You Win")
                
            elif playerHand.getValue() < dealerHand.getValue():
                print("Dealer Wins")
                
            else:
                print("Tie")
            return True
        return False

g = Game()
g.play()
