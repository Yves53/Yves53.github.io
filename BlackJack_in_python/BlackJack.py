# coding=utf-8
import random


class Blackjack(object):
    cards = []
    card_deck = ["2♣ ", '3♣ ', '4♣ ', '5♣ ', '6♣ ', '7♣ ', '8♣ ', '9♣ ', '10♣ ', 'A♣ ', 'J♣ ', 'Q♣ ', 'K♣ ',
                 '2♦ ', '3♦ ', '4♦ ', '5♦ ', '6♦ ', '7♦ ', '8♦ ', '9♦ ', '10♦ ', 'A♦ ', 'J♦ ', 'Q♦ ', 'K♦ ',
                 '2♥ ', '3♥ ', '4♥ ', '5♥ ', '6♥ ', '7♥ ', '8♥ ', '9♥ ', '10♥ ', 'A♥ ', 'J♥ ', 'Q♥ ', 'K♥ ',
                 '2♠ ', '3♠ ', '4♠ ', '5♠ ', '6♠ ', '7♠ ', '8♠ ', '9♠ ', '10♠ ', 'A♠ ', 'J♠ ', 'Q♠ ', 'K♠ ']

    def __init__(self, bet_money=0, deposit=0, array=None, val=0, cards_value=0, answer='Y', d_cards_value=0,
                 d_cards=None, remove_ten_p=0, remove_ten_d=0, number=0, card=''):
        if array is None:
            array = []
        if d_cards is None:
            d_cards = []
        self.bet_money = bet_money
        self.deposit = deposit
        self.val = val
        self.array = array
        self.cards_value = cards_value
        self.d_cards = d_cards
        self.d_cards_value = d_cards_value
        self.answer = answer
        self.remove_ten_p = remove_ten_p
        self.remove_ten_d = remove_ten_d
        self.number = number
        self.card = card

    def set_deposit(self):
        self.deposit = int(raw_input('$'))

    def set_bet_money(self):
        self.bet_money = int(raw_input('$'))

    def hit_card(self):  # Method to deal cards
        while True:
            self.val = random.randint(0, 51)  # randomly choose a number between 0 and 51
            self.card = Blackjack.card_deck[self.val]  # This gets the corresponding card in "card_deck"

            if self.card not in self.array:  # keeps looping if the randomly chosen card is already in the "array"
                self.array.append(self.card)  # Add the card in the array so that it cannot be dealt again
                break
        return self.card  # return the card to the caller

    # end method to deal cards  ##### Method to calculate the value of a card #####

    def card_value(self, a):
        a = a + 1
        self.number = 0  # Initialize "number " as an integer
        if a == 1 or a == 14 or a == 27 or a == 40:  # These numbers represent the position of cards in the "card_deck"
            self.number = 2  # and this is the value of that card
        elif a == 2 or a == 15 or a == 28 or a == 41:
            self.number = 3
        elif a == 3 or a == 16 or a == 29 or a == 42:
            self.number = 4
        elif a == 4 or a == 17 or a == 30 or a == 43:
            self.number = 5
        elif a == 5 or a == 18 or a == 31 or a == 44:
            self.number = 6
        elif a == 6 or a == 19 or a == 32 or a == 45:
            self.number = 7
        elif a == 7 or a == 20 or a == 33 or a == 46:
            self.number = 8
        elif a == 8 or a == 21 or a == 34 or a == 47:
            self.number = 9
        elif a == 9 or a == 22 or a == 35 or a == 48:
            self.number = 10
        elif a == 10 or a == 23 or a == 36 or a == 49:
            self.number = 11
        elif a == 11 or a == 24 or a == 37 or a == 50:
            self.number = 10
        elif a == 12 or a == 25 or a == 38 or a == 51:
            self.number = 10
        elif a == 13 or a == 26 or a == 39 or a == 52:
            self.number = 10
        return self.number
    # End method to calculate the value of a card #####

    # player's card block #####
    def cards_total_value(self, v=0):
        self.cards_value += int(v)  # This add the cards values
        if self.cards_value > 21:  # This statement execute when the total value of cards exceed 21
            self.cards_value -= self.remove_ten_p  # If 1 of the cards is an A that was counted as 11, 10 is subtracted
            self.remove_ten_p = 0  # This value is then reset so that it doesn't keep subtracting 10
        return int(self.cards_value)  # Variable to display the total value of the player's cards.

    def player_cards(self, c):  # This method add the cards that are dealt to the array "cards" when called
        self.cards.append(c)

    def print_player_cards(self):  # This method print the string of cards that was dealt
        player_card = ''
        for i in self.cards:
            player_card += i
        return player_card
    # end player's cards block #####

    # start dealer's cards block #####
    def d_cards_total_value(self, d=0):
        self.d_cards_value += int(d)
        if self.d_cards_value > 21:
            self.d_cards_value -= self.remove_ten_d
            self.remove_ten_d = 0
        return self.d_cards_value

    def dealer_cards(self, c):
        self.d_cards.append(c)

    def print_dealer_cards(self):
        dealer_card = " "
        for i in self.d_cards:
            dealer_card += i
        return dealer_card
        # end dealer's cards block #####


# ***************************************** end Black_jack class *************************************************

bj = Blackjack()
total_won = 0
total_lost = 0
print 'How much do you want to deposit?'
bj.set_deposit()
total_deposit = bj.deposit  # *****************************************************************
if bj.deposit <= 0:  # This statement check to make sure the player entered a valid amount
    while True:
        print 'INVALID!Please enter an amount more than $0'
        bj.set_deposit()
        if bj.deposit > 0:
            break
# ***************************** This block repeats as log as the player wants to play again ###########################
while True:
    # reset the deck if there are 10 cards or less left in it
    if len(bj.array) >= 42:
        print "There are only ", (52 - len(bj.array)), " cards left in the deck." \
                                                       "\nThe game will continue with a new deck of cards"
        bj.array = []  # This reset the array containing played cards

    # reset values for the next deal
    bj.cards = []
    bj.d_cards = []
    bj.cards_value = 0
    bj.d_cards_value = 0
    bj.remove_ten_p = 0
    bj.remove_ten_d = 0
    print "You have $", bj.deposit, "! \nHow much do you want to bet?"
    bj.set_bet_money()

    # Make sure the bet does not exceed the current balance
    while bj.bet_money > bj.deposit or bj.bet_money <= 0:
        print "INVALID!Please enter an amount that does not exceed $", bj.deposit
        bj.set_bet_money()

    for _ in range(2):  # Player's first two card
        first_cards = bj.hit_card()  # call the method to deal a random card
        bj.player_cards(first_cards)  # This method keeps this player's cards in the array "cards"
        value = bj.card_value(bj.val)
        # value of Ace
        if value == 11:
            if bj.cards_value + 11 > 21:
                value = 1
        # end value of Ace

        if value == 11:
            bj.remove_ten_p = 10

        bj.cards_total_value(value)
        # end Player's first two card

    print "Your cards are:", bj.print_player_cards()  # print the player's cards
    print "Their value is: ", bj.cards_total_value()  # And the value
    if bj.cards_total_value() == 21:  # Display if the first two cards add up to 21
        print 'BLACKJACK!'

    # dealer's first card
    elif bj.cards_total_value() < 21:  # This statement execute only if the player's first 2 cards did not add up to 21
        d_card = bj.hit_card()
        bj.dealer_cards(d_card)
        d_value = bj.card_value(bj.val)
        if d_value == 11:
            bj.remove_ten_d = 10
        bj.d_cards_total_value(d_value)
        print "The dealer's card is:", bj.print_dealer_cards()
        print "its value is: ", bj.d_cards_total_value()
    # end dealer's first card

        while True:  # Hit loop
            print 'HIT(H) or STAND(S)'
            bj.answer = raw_input().upper()
            if bj.answer not in ('H', 'S'):  # make sure the answer is H or S
                while True:
                    print 'Please enter a valid answer; H for Hit or S for Stand'
                    bj.answer = raw_input().upper()
                    if bj.answer in ('H', 'S'):
                        break

            if bj.answer == 'H':
                h_card = bj.hit_card()
                bj.player_cards(h_card)
                h_value = bj.card_value(bj.val)
                # value of Ace
                if h_value == 11:
                    if (bj.cards_value + 11) > 21:
                        h_value = 1
                if h_value == 11:  # When ace is counted as 11, "remove_ten_d" is assigned the value of 10 so that
                    # it can be subtracted if the total value is over 21
                    bj.remove_ten_p = 10
                # end value of Ace
                bj.cards_total_value(h_value)
                print "Your cards are:", bj.print_player_cards(), "\nTheir value is: ", bj.cards_total_value()

                if bj.cards_total_value() > 21:
                    print 'BUST!'

            if bj.answer == 'S' or bj.cards_total_value() >= 21:
                break  # end while , break loop when answer is STAND(S)
                # end if statement

        # start dealer's card block #####
        if bj.cards_total_value() < 21:  # Execute if the player's cards did not add up to 21
            while True:
                dd_card = bj.hit_card()
                bj.dealer_cards(dd_card)
                dd_value = bj.card_value(bj.val)
                if dd_value == 11:
                    if bj.d_cards_value + 11 > 21:
                        dd_value = 1
                if dd_value == 11:  # When ace is counted as 11, "remove_ten_d" is assigned the value of 10
                    # so that it can be subtracted if the total value is over 21
                    bj.remove_ten_d = 10
                bj.d_cards_total_value(dd_value)

                if bj.d_cards_total_value() > bj.cards_total_value() or bj.d_cards_total_value() >= 21 or bj.d_cards_total_value() == bj.cards_total_value:
                    print "The dealer's cards are:", bj.print_dealer_cards()
                    print "Their value is: ", bj.d_cards_total_value()
                    break
        # end dealer's card block #####

    # check if the player won, lost or it's a push; then update the balance accordingly #####
    if bj.cards_total_value() == 21 or bj.d_cards_total_value() > 21 > bj.cards_total_value():  # It's a WIN
        print 'You won!'
        total_won += bj.bet_money
        bj.deposit += bj.bet_money
        print "Your new balance is: $", bj.deposit

    elif bj.cards_total_value() == bj.d_cards_total_value():  # It's a PUSH
        print 'PUSH!'
        print "Your balance is still: $", bj.deposit

    else:  # It's a losing deal
        print 'You Lost!'
        bj.deposit -= bj.bet_money
        total_lost += bj.bet_money
        print "Your new balance is: $", bj.deposit
    # ******* end check for deals #####

    print "There are ", (52 - len(bj.array)), " cards left in the deck"  # Keep track of cards in the deck
    print 'Do you want to Play again? Yes(Y) or No(N)'  # ask the player if they want to continue playing, after a deal
    pa_answer = raw_input().upper()
    if pa_answer not in ('N', 'Y'):  # make sure the answer is Y or N
        while True:
            print 'Please enter a valid answer; Y for Yes or N for No'
            pa_answer = raw_input().upper()
            print pa_answer
            if pa_answer in ('N', 'Y'):
                break

    # ****** Executes when the balance is zero, and the player wants to keep playing after adding money #####
    if bj.deposit == 0 and pa_answer == 'Y':
        print 'You are out of money; do you want to add more?'
        print 'Please press Y for Yes or N for No'
        deposit_answer = raw_input().upper()  # get the player's answer

        if deposit_answer not in ('N', 'Y'):  # if statement to make sure the answer is Y or N
            while True:
                print 'Please enter a valid answer; Y for Yes or N for No'
                deposit_answer = raw_input().upper()
                if deposit_answer in ('N', 'Y'):
                    break

        if deposit_answer == 'Y':  # This statement execute when the player choose to add money
            print 'How much do you want to deposit?'
            bj.set_deposit()
            total_deposit += bj.deposit
            if bj.deposit <= 0:
                while True:
                    print 'Please enter a valid amount, more than $0'
                    bj.set_deposit()
                    if bj.deposit > 0:
                        break

    if pa_answer == 'N' or bj.deposit == 0:  # Exit the loop (game) when the player answers No (N) or enter 0
        break

# ************************************ End play again! #####################################################
print "********SUMMARY********"
print "You deposited a total of $", total_deposit
print "You won .................$", total_won
print "You lost ................$", total_lost
if (total_deposit + total_won - total_lost) > total_deposit:
    print "This was a WINNING GAME!"
    print "Overall, You won ....$", (total_won - total_lost)
elif total_won == total_lost:
    print "You didn't win or loose anything"
else:
    print "This was a LOOSING GAME!"
    print "Overall, you lost .......$", (total_lost - total_won)
print 'Thanks for playing!'
print 'GAME OVER!'
