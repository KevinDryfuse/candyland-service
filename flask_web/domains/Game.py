from flask_web.domains.Board import Board
from flask_web.domains.Deck import Deck
from flask_web.enums.ColorCount import ColorCount
from flask_web.enums.Type import Type
import sys


class Game:

    def __init__(self, players):
        self.players = players
        self.deck = Deck()
        self.board = Board()
        self.turn = 1
        self.there_is_a_winner = False
        self.winner = None

    def get_players(self):
        return self.players

    def play_game(self):

        player_iterator = 0

        # TODO: Make this WAAAAAY cleaner
        while player_iterator <= (self.players.get_total_players() - 1):
            player = self.players.get_player(player_iterator)
            card = self.deck.take()

            if player.get_lose_a_turn_flag():
                # print('Player ' + player.name + ' has lost this turn!', file=sys.stderr)
                player.set_lose_a_turn_flag(False)
            else:
                # print('Player ' + player.name + ' is on turn number ' + str(
                #     self.turn) + ' and took card ' + card.get_card_info(), file=sys.stderr)
                # print('Starting from position ' + str(player.position) + ' which is ' + self.board.get_space(
                #     player.position).get_space_info(), file=sys.stderr)
                # print('There are ' + str(
                #     self.board.get_number_of_spaces() - player.position) + ' spaces remaining until this player wins!',
                #       file=sys.stderr)

                if card.card_type == Type.character:
                    player.set_position(0)

                if card.color_count == ColorCount.double:
                    moves_remaining = 1
                else:
                    moves_remaining = 0

                while player.position <= self.board.get_number_of_spaces():
                    player.set_position(player.position + 1)
                    # print('There are ' + str(
                    #     self.board.get_number_of_spaces() - player.position) + ' spaces remaining until this player wins!',
                    #       file=sys.stderr)
                    if player.position >= self.board.get_number_of_spaces():
                        # print('PLAYER ' + player.name + ' HAS WON!', file=sys.stderr)
                        self.there_is_a_winner = True
                        player.add_victory()
                        self.winner = player
                        break

                    space = self.board.get_space(player.position)

                    if card.card_type == Type.color:
                        if (space.space_type == Type.color) & (space.color == card.color):
                            # print('Player ' + player.name + ' has landed on space ' + space.color.name + '!',
                            #       file=sys.stderr)
                            if (space.skip_ahead != None):
                                skip_to = (player.position + space.skip_ahead)
                                # print('Player ' + player.name + ' is skipping to space ' + str(skip_to) + '!',
                                #       file=sys.stderr)
                                player.set_position(skip_to)
                            if (space.lose_a_turn):
                                # print('Player ' + player.name + ' has lost a turn!', file=sys.stderr)
                                player.set_lose_a_turn_flag(True)
                            if moves_remaining == 0:
                                break

                            moves_remaining = 0
                            # print('Player ' + player.name + ' thinks moving twice is twice as nice!', file=sys.stderr)

                    elif card.card_type == Type.character:
                        if (space.space_type == Type.character) & (space.character == card.character):
                            # print('Player ' + player.name + ' has landed on space ' + space.character.name + '!',
                            #       file=sys.stderr)
                            break

            player_iterator += 1
            if player_iterator > (self.players.get_total_players() - 1):
                self.turn += 1
                player_iterator = 0
            if self.there_is_a_winner:
                for player in self.players:
                    player.set_lose_a_turn_flag(False)
                break
