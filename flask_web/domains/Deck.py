import random
import sys

from flask_web.domains.Card import Card
from flask_web.enums.Type import Type
from flask_web.enums.Character import Character
from flask_web.enums.Color import Color
from flask_web.enums.ColorCount import ColorCount


class Deck:

    def __init__(self):
        self.i = 0
        self.cards = []
        self.shuffle()

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.cards):
            self.i = self.i + 1
            return self.cards[self.i - 1]
        else:
            self.i = 0
            raise StopIteration

    def set_cards(self, cards):
        self.cards = cards

    def get_cards(self):
        return self.cards

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        print('SHUFFLE!!!', file=sys.stderr)
        random.shuffle(self.cards)

    def number_of_cards(self):
        return len(self.cards)

    def take(self):
        if self.number_of_cards() == 0:
            self.build()
            self.shuffle()
        return self.cards.pop(0)

    def build(self):
        self.add_card(
            Card(card_type=Type.color, color=Color.red, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.red, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.red, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.red, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.red, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.red, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.red, color_count=ColorCount.double, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.red, color_count=ColorCount.double, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.red, color_count=ColorCount.double, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.red, color_count=ColorCount.double, character=Character.none))

        self.add_card(
            Card(card_type=Type.color, color=Color.orange, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.orange, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.orange, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.orange, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.orange, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.orange, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.orange, color_count=ColorCount.double, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.orange, color_count=ColorCount.double, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.orange, color_count=ColorCount.double, character=Character.none))

        self.add_card(
            Card(card_type=Type.color, color=Color.yellow, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.yellow, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.yellow, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.yellow, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.yellow, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.yellow, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.yellow, color_count=ColorCount.double, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.yellow, color_count=ColorCount.double, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.yellow, color_count=ColorCount.double, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.yellow, color_count=ColorCount.double, character=Character.none))

        self.add_card(
            Card(card_type=Type.color, color=Color.green, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.green, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.green, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.green, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.green, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.green, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.green, color_count=ColorCount.double, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.green, color_count=ColorCount.double, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.green, color_count=ColorCount.double, character=Character.none))

        self.add_card(
            Card(card_type=Type.color, color=Color.blue, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.blue, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.blue, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.blue, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.blue, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.blue, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.blue, color_count=ColorCount.double, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.blue, color_count=ColorCount.double, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.blue, color_count=ColorCount.double, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.blue, color_count=ColorCount.double, character=Character.none))

        self.add_card(
            Card(card_type=Type.color, color=Color.purple, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.purple, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.purple, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.purple, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.purple, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.purple, color_count=ColorCount.single, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.purple, color_count=ColorCount.double, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.purple, color_count=ColorCount.double, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.purple, color_count=ColorCount.double, character=Character.none))
        self.add_card(
            Card(card_type=Type.color, color=Color.purple, color_count=ColorCount.double, character=Character.none))

        self.add_card(Card(card_type=Type.character, color=Color.none, color_count=ColorCount.none,
                           character=Character.mamma_ginger_tree))
        self.add_card(Card(card_type=Type.character, color=Color.none, color_count=ColorCount.none,
                           character=Character.mr_mint))
        self.add_card(Card(card_type=Type.character, color=Color.none, color_count=ColorCount.none,
                           character=Character.jolly))
        self.add_card(Card(card_type=Type.character, color=Color.none, color_count=ColorCount.none,
                           character=Character.gramma_nutt))
        self.add_card(Card(card_type=Type.character, color=Color.none, color_count=ColorCount.none,
                           character=Character.princess_lolly))
        self.add_card(Card(card_type=Type.character, color=Color.none, color_count=ColorCount.none,
                           character=Character.princess_frostine))
