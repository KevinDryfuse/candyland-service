
class Players:

    def __init__(self):
        self.i = 0
        self.players = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.players):
            self.i = self.i + 1
            return self.players[self.i - 1]
        else:
            self.i = 0
            raise StopIteration

    def add_player(self, player):
        self.players.append(player)

    def get_total_players(self):
        return len(self.players)

    def get_player(self, player_iterator):
        return self.players[player_iterator]
