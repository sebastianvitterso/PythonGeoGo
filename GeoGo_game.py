import random
from GeoGo_players import *


class Game:
    def __init__(self, playerlist):
        self.players = playerlist
        self.deck = []
        self.table_stack = []

    def shuffle_deck(self):
        tempdeck = []
        for letter in "abcdefghijklmnopqr":
            for number in [0, 1, 2, 3, 4]:
                tempdeck.append(Card(letter, number))
        for i in range(0, 90):
            # print(i)
            tempcard = tempdeck.pop(random.randint(0, 89 - i))
            self.deck.append(tempcard)

    def show_deck(self):
        print("Size of deck is " + str(len(self.deck)) + " cards.")
        print(self.deck)

    def get_deck_card(self):
        if len(self.deck) > 0:
            return self.deck.pop(0)
        elif len(self.table_stack) > 0:
            return self.table_stack.pop()
        else:
            raise RuntimeError("get_deck_card() called on empty deck and stack.")

    def get_table_stack_card(self):
        if len(self.table_stack) > 0:
            return self.table_stack.pop()
        elif len(self.deck) > 0:
            return self.deck.pop(0)
        else:
            raise RuntimeError("get_table_stack_card() called on empty deck and stack.")

    def view_table_stack_top(self):
        if len(self.table_stack) > 0:
            return self.table_stack[-1]
        else:
            return Card("s", -1)

    def add_to_stack(self, card):
        self.table_stack.append(card)

    def play_game(self):
        playernum = 0
        self.deck = []
        self.shuffle_deck()
        self.table_stack = []
        for player in self.players:
            player.game = self
            player.hand = []
            player.table = []
            for _ in range(0, 10):
                player.hand.append(self.deck.pop(0))
        while len(self.deck) > 0 or len(self.table_stack) > 0:
            # print("\n\nCards in deck: " + str(len(self.deck)))
            # print("Cards in table-stack: " + str(len(self.table_stack)))
            print("\nPlayer " + str(playernum) + ":")
            # self.players[playernum].show_hand()
            self.players[playernum].move()
            playernum += 1
            playernum = playernum % len(self.players)
        print("Scores:")
        scoretable = []
        for i in range(len(self.players)):
            print("Player" + str(i) + ": " + str(self.players[i].calculate_score()) + " pts.")
            scoretable.append(self.players[i].calculate_score())
        return scoretable


class Card:
    def __init__(self, letter, number): # 18 letters [a-r], 5 numbers [0-4] -> a stack holds 90 cards
        if letter in "abcdefghijklmnopqrs":
            self.letter = letter
        else:
            raise ValueError("Cards may only be of letter [a-s].")
        if number in [-1, 0, 1, 2, 3, 4]:
            self.number = number
        else:
            raise ValueError("Cards may only be of number [-1,4].")

    def __repr__(self):
        return "|" + self.letter + str(self.number) + "|"

    def __str__(self):
        return "|" + self.letter + str(self.number) + "|"


if __name__ == "__main__":
    player0 = DoubleDownPlayer()
    player1 = DoubleDownPlayer()
    player2 = DoubleDownPlayer()
    mygame = Game([player0, player1, player2])
    # player1.show_hand()
    # player2.show_hand()
    # mygame.show_deck()
    score_table = [0, 0, 0]
    for i in range(10):
        temp_table = mygame.play_game()
        for i in range(len(temp_table)):
            score_table[i] += temp_table[i]

    print()
    print(score_table)

