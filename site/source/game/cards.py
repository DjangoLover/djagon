import uuid


colors = ['red', 'green', 'blue', 'yellow']
values = [str(x) for x in range(1, 10)] * 2 + ['reverse', 'skip', 'draw-two'] * 2 + ['0']
wild_cards = [] #[{'color': 'black', 'value': 'wild'}] * 4
draw_four_cards = [] #[{'color': 'black', 'value': 'draw-four'}] * 4

SCORE_PICTURES = 10
SCORE_WILD = 20

def generate_cards():
    cards = wild_cards + draw_four_cards
    for col in colors:
        for val in values:
            cards.append({'color': col, 'value': val})
    for card in cards:
        card['id'] = str(uuid.uuid4())[-5:]
    return cards


def get_card_by_id(cards, card_id):
    for x in cards:
        if x["id"] == card_id:
            return x


def get_cards_score(card):
    if card['value'] in range(1, 10):
        return int(card['value'])
    elif card['value'] in ['reverse', 'skip', 'draw-two']:
        return SCORE_PICTURES
    else:
        return SCORE_WILD
