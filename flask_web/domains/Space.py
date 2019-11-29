from flask_web.enums.Color import Color
from flask_web.enums.Character import Character
from flask_web.enums.Type import Type


class Space:

    def __init__(self, space_type, color=None, character=None, skip_ahead=None, lose_a_turn=False):
        self.space_type = space_type
        self.skip_ahead = skip_ahead
        self.lose_a_turn = lose_a_turn

        if space_type == Type.character:
            if character == Character.none:
                raise ValueError('A character is not specified for a character type space!')

            self.color = Color.none
            self.character = character
        else:
            if color == Color.none:
                raise ValueError('A color is not specified for a color type space!')

            self.color = color
            self.character = Character.none

    def get_space_info(self):
        if self.space_type == Type.character:
            space_info = self.character.value
        else:
            space_info = self.color.value

        return space_info
