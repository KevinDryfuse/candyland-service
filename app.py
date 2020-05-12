from flask import Flask, render_template, make_response
from flask_web.domains.Players import Players


from flask_web.domains.Game import Game

app = Flask(__name__)

# TODO: Get this in a position where is can play n number of games
# TODO: Add endpoints to setup a game instead of the hardcoded values
# TODO: Add some visuals and track statistics
# TODO: All the things
@app.route('/CandyLand/<players>', methods=["GET"])
def single_game(players):
    players = Players(players)
    game = Game(players)
    game.play_game()
    print(game.winner.get_name())
    # return "Player " + game.winner.get_name() + " won the game!"
    return render_template('template.html', my_string=game.winner.get_name(), my_list=[0,1,2,3,4,5])


@app.route('/CandyLand/<players>/games/<games>', methods=["GET"])
def more_than_one_game(players, games):
    game_players = Players(players)

    game_number = 1
    while game_number <= int(games):
        game = Game(game_players)
        game.play_game()
        game_number += 1

    return_string = "For " + games + " games: \n"
    for player in game.get_players():
        return_string += " - Player " + player.get_name() + " won the game " + str(player.victory_count) + " times!\n"

    response = make_response(return_string, 200)
    response.headers["Content-Type"] = "application/json"
    return response


if __name__ == '__main__':

    app.run(debug=True,
            host='0.0.0.0')

