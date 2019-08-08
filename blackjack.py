'''
A simulation of blackjack GAME

'''

import random

#DEFINING suits rank and values

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'King', 'Queen', 'Jack', 'Ace']
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
          'Nine':9, 'Ten':10, 'King':10, 'Queen':10, 'Jack':10, 'Ace':11}

player = ""  #global variable

class Card():

    '''
    Creates a 'Card' object

    '''


    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)

class Deck():

    '''
    Creates a 'Deck' object

    '''

    def __init__(self):
        self.cardset = []
        for suit in suits:
            for rank in ranks:
                self.cardset.append(Card(suit, rank))

    def __str__(self):
        s = ''
        for card in self.cardset:
            s = s+card.__str__()+'\n'
        return s

    def shuffleset(self):
        random.shuffle(self.cardset)

    def deal(self):
        return self.cardset.pop()

class Hand():

    '''
    Creates a 'Hand' object

    '''

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def addcard(self, card):
        self.cards.append(card)
        if card.rank == 'Ace':
            self.aces += 1

    def addvalue(self, card):
        self.value += values[card.rank]
        if self.value > 21 and card.rank == 'Ace':
            self.aces -= 1
            self.value -= 10

def print_some(hand_dealer, hand_player):

    '''
    Displays the player's cards and the dealer's cards without including dealer's 1st card

    '''

    print("\n"+player+"\'s Hand:\n", *hand_player.cards, sep='\n ')
    print("\nDealer's hand:")
    print("\n"+"1st card hidden", '\n', hand_dealer.cards[1])


def print_all(hand_dealer, hand_player):

    '''
    Displays all the cards of dealer and the player

    '''
    print("\n"+player+"\'s Hand:\n", *hand_player.cards, sep='\n ')
    print(player+"\'s score: "+ str(hand_player.value))
    print("\nDealer's Hand:\n", *hand_dealer.cards, sep='\n ')
    print("Dealer's score: "+ str(hand_dealer.value))




def game():

    '''
    Function for game play...

    '''

    amount = 0
    


    # Introduction of game and minor rules

    print("\nWELCOME TO THE GAME OF BLACK JACK!\n")
    print("This game involves a manual player and a computer dealer.")
    print("Get as close to 21 as you can without going over!")
    print("Computer dealer hits until it reaches 17. Aces count as 1 or 11.\n")

    player = input("Enter your name\n")  #Player's name

    # ASKING THE PLAYER FOR THEIR FUNDS

    while True:


        try:
            amount = int(input("\nEnter your total available chips\n"))
        except:
            print("\nEnter an integer value\n")
        else:
            break

    playing = 'y'   # Variable for controlling the following outer while loop

    # MAIN GAME PLAY

    while playing == 'y':

        bet = 0

        if amount > 0:

            while True:
                try:

                    bet = int(input("\nEnter your bet\n"))
                except:
                    print("\nEnter an integer value\n")
                else:
                    if bet <= amount:
                        break
                    else:
                        print("\nHey! You don't have enough chips!\n")

            deck = Deck()
            deck.shuffleset()
            hand_player = Hand()
            hand_dealer = Hand()

            for i in range(2):
                card = deck.deal()
                hand_player.addcard(card)
                hand_player.addvalue(card)
                card = deck.deal()
                hand_dealer.addcard(card)
                hand_dealer.addvalue(card)

            print_some(hand_dealer, hand_player)

            ch = ''
            while True:

                ch = input("\n"+player+", Would you like to hit or stand? h/s\n")
                if ch == 'h':
                    card = deck.deal()
                    hand_player.addcard(card)
                    hand_player.addvalue(card)
                    print_some(hand_dealer, hand_player)
                    if hand_player.value > 21:
                        print("\n"+player, ', you have busted! Dealer wins without even hitting!')
                        amount -= bet
                        break
                elif ch == 's':
                    print("\nYou has chosen to stay. Dealer will hit now!\n")
                    break
                else:
                    print("\nPlease enter a valid choice\n")



            if hand_player.value <= 21:
                print("\nDealer will now show the hidden card\n")
                print_all(hand_dealer, hand_player)
                if hand_dealer.value < 17:
                    print("\nDealer will now hit until it reaches a score of 17\n")
                while hand_dealer.value < 17:
                    card = deck.deal()
                    hand_dealer.addcard(card)
                    hand_dealer.addvalue(card)
                    print_all(hand_dealer, hand_player)
                if hand_dealer.value > 21:
                    print("\nDealer has busted. {}, you have won\n".format(player))
                    amount += bet
                elif hand_dealer.value > hand_player.value:
                    print("Dealer has won!")
                    amount -= bet
                elif hand_dealer.value < hand_player.value:
                    print(player+", you have won!")
                    amount += bet
                else:
                    print("It's a draw!")

            print("\n"+player+", your chips stand at \n"+str(amount))

        else:
            print("\nSorry! You have no chips to play anymore!!\n")
            break



        playing = input("\nDo You want to play again? yes/no\n")
        playing = playing[0].lower()

game()
print("\nThanks for playing!\n")
