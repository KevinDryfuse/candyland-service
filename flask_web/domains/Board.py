from flask_web.domains.Space import Space
from flask_web.enums.Color import Color
from flask_web.enums.Type import Type
from flask_web.enums.Character import Character


class Board:

    def __init__(self):
        self.spaces = []
        self.build()

    def build(self):
        self.add_space(Space(space_type=Type.color, color=Color.red))
        self.add_space(Space(space_type=Type.color, color=Color.purple))
        self.add_space(Space(space_type=Type.color, color=Color.yellow))
        self.add_space(Space(space_type=Type.color, color=Color.blue))
        self.add_space(Space(space_type=Type.color, color=Color.orange, skip_ahead=54))
        self.add_space(Space(space_type=Type.color, color=Color.green))

        self.add_space(Space(space_type=Type.color, color=Color.red))
        self.add_space(Space(space_type=Type.color, color=Color.purple))
        self.add_space(Space(space_type=Type.character, character=Character.mamma_ginger_tree))
        self.add_space(Space(space_type=Type.color, color=Color.yellow))
        self.add_space(Space(space_type=Type.color, color=Color.blue))
        self.add_space(Space(space_type=Type.color, color=Color.orange))
        self.add_space(Space(space_type=Type.color, color=Color.green))

        self.add_space(Space(space_type=Type.color, color=Color.red))
        self.add_space(Space(space_type=Type.color, color=Color.purple))
        self.add_space(Space(space_type=Type.color, color=Color.yellow))
        self.add_space(Space(space_type=Type.color, color=Color.blue))
        self.add_space(Space(space_type=Type.color, color=Color.orange))
        self.add_space(Space(space_type=Type.color, color=Color.green))

        self.add_space(Space(space_type=Type.character, character=Character.mr_mint))
        self.add_space(Space(space_type=Type.color, color=Color.red))
        self.add_space(Space(space_type=Type.color, color=Color.purple))
        self.add_space(Space(space_type=Type.color, color=Color.yellow))
        self.add_space(Space(space_type=Type.color, color=Color.blue))
        self.add_space(Space(space_type=Type.color, color=Color.orange))
        self.add_space(Space(space_type=Type.color, color=Color.green))

        self.add_space(Space(space_type=Type.color, color=Color.red))
        self.add_space(Space(space_type=Type.color, color=Color.purple))
        self.add_space(Space(space_type=Type.color, color=Color.yellow))
        self.add_space(Space(space_type=Type.color, color=Color.blue))
        self.add_space(Space(space_type=Type.color, color=Color.orange))
        self.add_space(Space(space_type=Type.color, color=Color.green))

        self.add_space(Space(space_type=Type.color, color=Color.red))
        self.add_space(Space(space_type=Type.color, color=Color.purple))
        self.add_space(Space(space_type=Type.color, color=Color.yellow, character=None, skip_ahead=10))
        self.add_space(Space(space_type=Type.color, color=Color.blue))
        self.add_space(Space(space_type=Type.color, color=Color.orange))
        self.add_space(Space(space_type=Type.color, color=Color.green))

        self.add_space(Space(space_type=Type.color, color=Color.red))
        self.add_space(Space(space_type=Type.color, color=Color.purple))
        self.add_space(Space(space_type=Type.color, color=Color.yellow))
        self.add_space(Space(space_type=Type.character, character=Character.jolly))
        self.add_space(Space(space_type=Type.color, color=Color.blue))
        self.add_space(Space(space_type=Type.color, color=Color.orange))
        self.add_space(Space(space_type=Type.color, color=Color.green))

        self.add_space(Space(space_type=Type.color, color=Color.red, lose_a_turn=True))
        self.add_space(Space(space_type=Type.color, color=Color.purple))
        self.add_space(Space(space_type=Type.color, color=Color.yellow))
        self.add_space(Space(space_type=Type.color, color=Color.blue))
        self.add_space(Space(space_type=Type.color, color=Color.orange))
        self.add_space(Space(space_type=Type.color, color=Color.green))

        self.add_space(Space(space_type=Type.color, color=Color.red))
        self.add_space(Space(space_type=Type.color, color=Color.purple))
        self.add_space(Space(space_type=Type.color, color=Color.yellow))
        self.add_space(Space(space_type=Type.color, color=Color.blue))
        self.add_space(Space(space_type=Type.color, color=Color.orange))
        self.add_space(Space(space_type=Type.color, color=Color.green))

        self.add_space(Space(space_type=Type.color, color=Color.red))
        self.add_space(Space(space_type=Type.color, color=Color.purple))
        self.add_space(Space(space_type=Type.color, color=Color.yellow))
        self.add_space(Space(space_type=Type.color, color=Color.blue))
        self.add_space(Space(space_type=Type.color, color=Color.orange))
        self.add_space(Space(space_type=Type.color, color=Color.green))

        self.add_space(Space(space_type=Type.color, color=Color.red))
        self.add_space(Space(space_type=Type.color, color=Color.purple))
        self.add_space(Space(space_type=Type.color, color=Color.yellow))
        self.add_space(Space(space_type=Type.color, color=Color.blue))
        self.add_space(Space(space_type=Type.color, color=Color.orange))
        self.add_space(Space(space_type=Type.character, character=Character.gramma_nutt))
        self.add_space(Space(space_type=Type.color, color=Color.green))

        self.add_space(Space(space_type=Type.color, color=Color.red))
        self.add_space(Space(space_type=Type.color, color=Color.purple))
        self.add_space(Space(space_type=Type.color, color=Color.yellow))
        self.add_space(Space(space_type=Type.color, color=Color.blue))
        self.add_space(Space(space_type=Type.color, color=Color.orange))
        self.add_space(Space(space_type=Type.color, color=Color.green))

        self.add_space(Space(space_type=Type.color, color=Color.red))
        self.add_space(Space(space_type=Type.color, color=Color.purple))
        self.add_space(Space(space_type=Type.color, color=Color.yellow))
        self.add_space(Space(space_type=Type.color, color=Color.blue))
        self.add_space(Space(space_type=Type.color, color=Color.orange))
        self.add_space(Space(space_type=Type.color, color=Color.green))

        self.add_space(Space(space_type=Type.color, color=Color.red))
        self.add_space(Space(space_type=Type.color, color=Color.purple))
        self.add_space(Space(space_type=Type.color, color=Color.yellow))
        self.add_space(Space(space_type=Type.color, color=Color.blue, lose_a_turn=True))
        self.add_space(Space(space_type=Type.color, color=Color.orange))
        self.add_space(Space(space_type=Type.color, color=Color.green))

        self.add_space(Space(space_type=Type.color, color=Color.red))
        self.add_space(Space(space_type=Type.color, color=Color.purple))
        self.add_space(Space(space_type=Type.color, color=Color.yellow))
        self.add_space(Space(space_type=Type.character, character=Character.princess_lolly))
        self.add_space(Space(space_type=Type.color, color=Color.blue))
        self.add_space(Space(space_type=Type.color, color=Color.orange))
        self.add_space(Space(space_type=Type.color, color=Color.green))

        self.add_space(Space(space_type=Type.color, color=Color.red))
        self.add_space(Space(space_type=Type.color, color=Color.purple))
        self.add_space(Space(space_type=Type.color, color=Color.yellow))
        self.add_space(Space(space_type=Type.color, color=Color.blue))
        self.add_space(Space(space_type=Type.color, color=Color.orange))
        self.add_space(Space(space_type=Type.color, color=Color.green))

        self.add_space(Space(space_type=Type.character, character=Character.princess_frostine))
        self.add_space(Space(space_type=Type.color, color=Color.red))
        self.add_space(Space(space_type=Type.color, color=Color.purple))
        self.add_space(Space(space_type=Type.color, color=Color.yellow))
        self.add_space(Space(space_type=Type.color, color=Color.blue))
        self.add_space(Space(space_type=Type.color, color=Color.orange))
        self.add_space(Space(space_type=Type.color, color=Color.green))

        self.add_space(Space(space_type=Type.color, color=Color.red))
        self.add_space(Space(space_type=Type.color, color=Color.purple))
        self.add_space(Space(space_type=Type.color, color=Color.yellow))
        self.add_space(Space(space_type=Type.color, color=Color.blue))
        self.add_space(Space(space_type=Type.color, color=Color.orange))
        self.add_space(Space(space_type=Type.color, color=Color.green))

        self.add_space(Space(space_type=Type.color, color=Color.red))
        self.add_space(Space(space_type=Type.color, color=Color.purple))
        self.add_space(Space(space_type=Type.color, color=Color.yellow, lose_a_turn=True))
        self.add_space(Space(space_type=Type.color, color=Color.blue))
        self.add_space(Space(space_type=Type.color, color=Color.orange))
        self.add_space(Space(space_type=Type.color, color=Color.green))

        self.add_space(Space(space_type=Type.color, color=Color.red))
        self.add_space(Space(space_type=Type.color, color=Color.purple))
        self.add_space(Space(space_type=Type.color, color=Color.yellow))
        self.add_space(Space(space_type=Type.color, color=Color.blue))
        self.add_space(Space(space_type=Type.color, color=Color.orange))
        self.add_space(Space(space_type=Type.color, color=Color.green))

        self.add_space(Space(space_type=Type.color, color=Color.red))
        self.add_space(Space(space_type=Type.color, color=Color.purple))
        self.add_space(Space(space_type=Type.color, color=Color.yellow))
        self.add_space(Space(space_type=Type.color, color=Color.blue))
        self.add_space(Space(space_type=Type.color, color=Color.orange))
        self.add_space(Space(space_type=Type.color, color=Color.green))

        self.add_space(Space(space_type=Type.color, color=Color.red))

    def add_space(self, space):
        self.spaces.append(space)

    def get_space(self, index):
        return self.spaces[index]

    def get_number_of_spaces(self):
        return len(self.spaces)