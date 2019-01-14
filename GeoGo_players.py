import random
from GeoGo_game import *


class Player:
    def __init__(self):
        self.hand = []
        self.table = []
        self.game = None

    def calculate_score(self):
        scoresum = 0
        letterdict = dict((key, 0) for key in "abcdefghijklmnopqr")
        for card in self.table:
            letterdict[card.letter] += 1
        for letter, amount in letterdict.items():
            if amount == 0:
                pass
            elif amount == 1:
                scoresum -= 5
            elif amount == 2:
                scoresum -= 2
            elif amount == 3:
                pass
            elif amount == 4:
                scoresum += 2
            elif amount == 5:
                scoresum += 5
            else:
                raise ValueError("Too few or many cards of one type on players table.")
        return scoresum

    def show_hand(self):
        print("Hand of size " + str(len(self.hand)) + ":")
        print(self.hand)

    def move(self):
        self.lay_card()
        self.pick_card()

    def lay_card(self):
        pass

    def pick_card(self):
        pass

    def lay_card_on_table(self, hand_index):
        self.table.append(self.hand.pop(hand_index))

    def lay_card_on_stack(self, hand_index):
        self.game.add_to_stack(self.hand.pop(hand_index))

    def pull_card_from_deck(self):
        self.hand.append(self.game.get_deck_card())

    def pull_card_from_stack(self):
        self.hand.append(self.game.get_table_stack_card())


class AlwaysDownPlayer(Player):  # Always lays them down, even if he only has one of each "letter"
    def __init__(self):
        Player.__init__(self)

    def lay_card(self):
        tabledict = dict((key, 0) for key in "abcdefghijklmnopqrs")
        for card in self.table:
            tabledict[card.letter] += 1
        # print(len(self.hand))
        for card_index in range(0, len(self.hand)):
            if tabledict[self.hand[card_index].letter] > 0:
                # print(card_index)
                # print("Laid card " + str(self.hand[card_index]) + "on own table.")
                self.lay_card_on_table(card_index)
                return
        max_card_index = 0
        max_letter_count = 0
        for card_index in range(len(self.hand)):
            if tabledict[self.hand[card_index].letter] > max_letter_count:
                max_card_index = card_index
                max_letter_count = tabledict[self.hand[card_index].letter]
        self.lay_card_on_table(max_card_index)
        # print("Laid card " + str(self.hand[max_card_index]) + "on own table.")
        return

    def pick_card(self):
        tabledict = dict((key, 0) for key in "abcdefghijklmnopqrs")
        for card in self.table:
            tabledict[card.letter] += 1
        for card in self.hand:
            tabledict[card.letter] += 1
        if tabledict[self.game.view_table_stack_top().letter] > 0:
            self.pull_card_from_stack()
            return
        else:
            self.pull_card_from_deck()


class DoubleDownPlayer(Player):  # Lays down if 2 or more of a card, else lays it out.
    def __init__(self):
        Player.__init__(self)

    def lay_card(self):
        tabledict = dict((key, 0) for key in "abcdefghijklmnopqrs")
        for card in self.table:
            tabledict[card.letter] += 1
        # print(len(self.hand))
        for card_index in range(0, len(self.hand)):
            if tabledict[self.hand[card_index].letter] > 0:
                print("Laying down.")
                print("Hand: " + str(self.hand))
                print("Table: " + str(self.table))
                print("Stack Top: " + str(self.game.view_table_stack_top()))
                print(self.hand[card_index])
                self.lay_card_on_table(card_index)
                return

        for card in self.hand:
            tabledict[card.letter] += 1
        max_card_index = 0
        max_letter_count = 0
        for card_index in range(len(self.hand)):
            if tabledict[self.hand[card_index].letter] > max_letter_count:
                max_card_index = card_index
                max_letter_count = tabledict[self.hand[card_index].letter]
        if max_letter_count >= 3:
            print("Laid card " + str(self.hand[max_card_index]) + "on own table.")
            self.lay_card_on_table(max_card_index)
            return

        enemytabledict = dict((key, 0) for key in "abcdefghijklmnopqrs")
        for player in self.game.players:
            if player is not self:
                for card in player.table:
                    enemytabledict[card.letter] += 1
        min_card_index = 0
        min_letter_count = 5
        for card_index in range(len(self.hand)):
            if enemytabledict[self.hand[card_index].letter] < min_letter_count:
                min_card_index = card_index
                min_letter_count = enemytabledict[self.hand[card_index].letter]
        self.game.add_to_stack(min_card_index)

    def pick_card(self):
        tabledict = dict((key, 0) for key in "abcdefghijklmnopqrs")
        print("HERE PROBLEM " + str(self.game.view_table_stack_top()))
        for card in self.table:
            tabledict[card.letter] += 1
        for card in self.hand:
            tabledict[card.letter] += 1
        if tabledict[self.game.view_table_stack_top().letter] > 0:
            self.pull_card_from_stack()
            return
        else:
            self.pull_card_from_deck()




