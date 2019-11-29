from flask_web.enums.Character import Character
from flask_web.enums.Type import Type
from flask_web.enums.ColorCount import ColorCount
from flask_web.enums.Color import Color


class Card:

    def __init__(self, card_type, color, color_count, character):
        self.card_type = card_type

        if card_type == Type.character:
            if character == Character.none:
                raise ValueError('A character is not specified for a character type card!')

            self.color = Color.none
            self.color_count = ColorCount.none
            self.character = character
        else:
            if color == Color.none:
                raise ValueError('A color is not specified for a color type card!')
            elif color_count == ColorCount.none:
                raise ValueError('A number is not specified for a color type card!')

            self.color = color
            self.color_count = color_count
            self.character = Character.none

    def get_type(self):
        return self.card_type

    def get_color(self):
        return self.color

    def get_color_count(self):
        return self.color_count

    def get_character(self):
        return self.character

    def get_card_info(self):
        if self.card_type == Type.character:
            card_info = self.character.value
        else:
            if self.color_count == ColorCount.double:
                card_info = self.color_count.value + ' ' + self.color.value
            else:
                card_info = self.color.value

        return card_info
