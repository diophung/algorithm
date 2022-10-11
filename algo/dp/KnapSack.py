# Initial Rules:
# * The game consists of 30 cards, where each card has a Value which is a number between 0-9 and a Color which is Red, Green, or Blue (RGB)
# * Each player gets 3 cards
# * Each game consists of some number of players, and winners are determined by who has the best Combo:
#     * Color Combo (3 cards same color) - 300 pts
#     * Value Combo (3 cards same value) - 30 pts
#     * Pair Combo (2 cards with same value, and 1 random card) - 10 pts
# * Scoring: best combo points

# Write the library required to play this game.  Don’t worry about UI, just create a main method to mimic the action of dealing the cards out to 10 players, score the players' hands, show (print) everyone's hand, and declare a winner.

import unittest

"""
Functional-requirements
    - deal cards to X (X=10) players
    - score the hands
    - print everyone's
    - declare winner

    Assumption: 30 card, 0-9, Color can change 
    Client-side:
    - Call main function --> do all the.

    Domain entity:
    - Player
    - Game
    - Card
    - Scoreboard (?)

Non-functional requirements
- no worries about scalability right now.

Strategy pattern to swap our new role
Strategy Factory to create new strategy if needed

"""


class Color:
    """ """

    def __init__(self, name):
        self._name = name


class CardValue:
    def __init__(self, val):
        self._val = val


class Player:
    MAX_CARD = 3

    def __init__(self, player_id, cards=[]):
        self._player_id = player_id
        self.is_winner = False
        self._cards = cards

    @property
    def cards(self):
        return self._cards

    def get_deal_card(self, new_card):
        if len(self._cards) == Player.MAX_CARD:
            raise ValueError("Already has max card: {} cards".format(Player.MAX_CARD))

        self._cards.append(new_card)

    def get_score(self):
        return


class Card:
    def __init__(self, color, value):
        """ """
        self._color = color
        self._value = value

    def get_color(self):
        return self._color

    def get_value(self):
        return self._value


class V1CardGameStrategy:
    COLOR_COMBO_SCORE = 300
    VALUE_COMBO_SCORE = 30
    PAIR_COMBO_SCORE = 10

    def deal_cards(self, players, cards):
        """ Randomly distribute 30 cards to 10 players """
        """
        cards: [] 
        ramdomize using Python built-in tools
        pop the cards , 3 cards to each player
        move the player with 3 cards out 
        continue

        """
        pass

    def _is_same_color(self, cards):
        return True

    def _is_same_value(self, cards):
        return True

    def _is_pair_combo(self, cards):
        return True

    def get_score(self, player):
        """
        #     * Color Combo (3 cards same color) - 300 pts
        #     * Value Combo (3 cards same value) - 30 pts
        #     * Pair Combo (2 cards with same value, and 1 random card) - 10 pts

        """
        total_score = 0
        my_cards = player.cards
        my_color = player.cards[0].get_color()
        my_value = player.cards[0].get_value()
        is_same_color = self._is_same_color(my_cards)
        is_same_value = self._is_same_value(my_cards)
        is_pair_combo = self._is_pair_combo(my_cards)

        if is_same_color:
            return V1CardGameStrategy.COLOR_COMBO_SCORE

        if is_same_value:
            return V1CardGameStrategy.VALUE_COMBO_SCORE

        if is_pair_combo:
            return V1CardGameStrategy.PAIR_COMBO_SCORE
        pass

    def get_players_hands(self, players):
        for p in players:
            print(p.cards)

    def get_winners(self, players):
        """
        return all winners with same score
        """
        winners = []
        sorted(players, key=lambda player: player.get_score())
        max_score = players[0].get_score()

        # go through all players
        for p in players:
            if max_score == p.get_score():
                winners.append(p)
            break

        return winners

    def play_game(self, players, cards):
        """
        - deal cards to X (X=10) players
        - score the hands
        - print everyone's hands
        - declare winner
        """
        self.deal_cards(players, cards)
        self.get_score(self, players)
        self.get_players_hands(self, players)
        winners = self.get_winner(players)
        print(winners)


class Game:
    def __init__(self, players, cards, game_strategy):
        """ """
        self._players = players
        self._cards = cards
        self._strategy = game_strategy

    def play_game(self):
        # Execute the strategy
        self._strategy.play_game()


class V1CardGameTest(unittest.TestCase):

    def test_edge_case_all_same_score(self):
        v1 = V1CardGameStrategy()
        players = []
        cards = []
        game = Game(players, cards, v1)
        game.play_game()

if __name__ == "__main__ ":
    unittest.main()







