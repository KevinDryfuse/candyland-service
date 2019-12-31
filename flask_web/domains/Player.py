
class Player:

    def __init__(self, name):
        self.name = name
        self.position = 0
        self.lose_a_turn_flag = False
        self.victory_count = 0

    def get_name(self):
        return self.name

    def set_position(self, position):
        self.position = position

    def get_lose_a_turn_flag(self):
        return self.lose_a_turn_flag

    def set_lose_a_turn_flag(self, lose_a_turn):
        self.lose_a_turn_flag = lose_a_turn

    def add_victory(self):
        self.victory_count += 1
