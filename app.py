from flask import Flask
from flask_web.enums.Character import Character
from flask_web.enums.CardType import CardType
from flask_web.enums.ColorCount import ColorCount
from flask_web.enums.Color import Color
from flask_web.domains.Card import Card
from flask_web.domains.Deck import Deck
import sys

app = Flask(__name__)


@app.route('/')
def hello_world():

    deck = Deck()

    deck.shuffle()

    for card in deck:
        print(card.get_card_info(), file=sys.stderr)

    deck.shuffle()

    print('SHUFFLED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! - ' + str(len(deck.cards)), file=sys.stderr)

    for card in deck:
        print(card.get_card_info(), file=sys.stderr)

    number_of_players = 3

    i = 1
    turn = 1
    while i <= number_of_players:

        print(i)
        print('Player ' + str(i) + ' is on turn number ' + str(turn))

        # Logic goes here!
        # Load a board (ordered list of somesort)








        i += 1
        turn += 1
        if i > number_of_players:
            i = 1
        if turn > 100:
            i = number_of_players + 1

    card = Card(card_type=CardType.character,
                color=Color.none,
                color_count=ColorCount.none,
                character=Character.gramma_nutt)

    return 'Hey, we have Flask in a Docker container! ' + card.get_card_info()


if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0')
