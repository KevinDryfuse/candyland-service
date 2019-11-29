import sys

from flask import Flask

from flask_web.domains.Board import Board
from flask_web.domains.Deck import Deck
from flask_web.domains.Player import Player
from flask_web.domains.Players import Players
from flask_web.enums.Type import Type

app = Flask(__name__)

# TODO: Add in functionality for 'double colors'
# TODO: Get this in a position where is can play n number of games
# TODO: Add endpoints to setup a game instead of the hardcoded values
# TODO: Add some visuals and track statistics
# TODO: All the things
@app.route('/')
def main():

    board = Board()

    deck = Deck()
    players = Players()
    players.add_player(Player('Ellison'))
    players.add_player(Player('Gina'))
    players.add_player(Player('Kevin'))
    turn = 1
    there_is_a_winner = False

    player_iterator = 0

    # TODO: Make this WAAAAAY cleaner
    while player_iterator <= (players.get_total_players() - 1):
        player = players.get_player(player_iterator)
        card = deck.take()

        if player.get_lose_a_turn_flag():
            print('Player ' + player.name + ' has lost this turn!', file=sys.stderr)
            player.set_lose_a_turn_flag(False)
        else:
            print('Player ' + player.name + ' is on turn number ' + str(turn) + ' and took card ' + card.get_card_info(), file=sys.stderr)
            print('Starting from position ' + str(player.position) + ' which is ' + board.get_space(player.position).get_space_info(), file=sys.stderr)
            print('There are ' + str(board.get_number_of_spaces() - player.position) + ' spaces remaining until this player wins!', file=sys.stderr)

            if card.card_type == Type.character:
                player.set_position(0)

            while player.position <= board.get_number_of_spaces():
                player.set_position(player.position + 1)
                print('There are ' + str(board.get_number_of_spaces() - player.position) + ' spaces remaining until this player wins!', file=sys.stderr)
                if player.position >= board.get_number_of_spaces():
                    print('PLAYER ' + player.name + ' HAS WON!', file=sys.stderr)
                    there_is_a_winner = True
                    break

                space = board.get_space(player.position)

                if card.card_type == Type.color:
                    if (space.space_type == Type.color) & (space.color == card.color):
                        print('Player ' + player.name + ' has landed on space ' + space.color.name + '!', file=sys.stderr)
                        if (space.skip_ahead != None):
                            skip_to = (player.position + space.skip_ahead)
                            print('Player ' + player.name + ' is skipping to space ' + str(skip_to) + '!', file=sys.stderr)
                            player.set_position(skip_to)
                        if (space.lose_a_turn):
                            print('Player ' + player.name + ' has lost a turn!', file=sys.stderr)
                            player.set_lose_a_turn_flag(True)
                        break
                elif card.card_type == Type.character:
                    if (space.space_type == Type.character) & (space.character == card.character):
                        print('Player ' + player.name + ' has landed on space ' + space.character.name + '!', file=sys.stderr)
                        break

        player_iterator += 1
        if player_iterator > (players.get_total_players() - 1):
            turn += 1
            player_iterator = 0
        if there_is_a_winner:
            break

    return 'Hey, we have Flask in a Docker container!'


if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0')
