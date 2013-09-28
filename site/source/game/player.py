import uuid


class Player(object):

    def __init__(self, name="", hand=[]):
        self.id = str(uuid.uuid4())[:6].upper()
        self.name = name
        self.hand = hand
        self.lamp = False

    def draw_cards(self, cards):
        self.hand = self.hand + cards

    @property
    def cards_number(self):
        return len(self.hand)
