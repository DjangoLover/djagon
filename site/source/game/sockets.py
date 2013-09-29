from socketio.namespace import BaseNamespace
from socketio.sdjango import namespace
from source.game.mechanics import GameMechanics
from source.game.models import GameTable


@namespace('/game')
class GameNamespace(BaseNamespace):

    def on_join_game(self, game_id):
        game = GameTable.get_game(game_id)
        if game is None: return # temp

        game_mechanics = GameMechanics(game, self.socket, self.session, self.ns_name)
        game_mechanics.on_join_game()

    def on_start_confirm(self, game_id):
        game = GameTable.get_game(game_id)
        if game is None:
            return

        player = game.players[self.session['player_id']]
        player.lamp = True
        game.save()

        game_mechanics = GameMechanics(game, self.socket, self.session, self.ns_name)

        are_all_players_confirmed = True
        for x in game.players:
            if game.players[x].lamp == False:
                are_all_players_confirmed = False

        if not are_all_players_confirmed:
            game_mechanics._send_initial_game_state()
        else:
            game_mechanics._send_game_start()

    def on_start_unconfirm(self, game_id):
        game = GameTable.get_game(game_id)
        if game is None:
            return

        player = game.players[self.session['player_id']]
        player.lamp = False
        game.save()

        game_mechanics = GameMechanics(game, self.socket, self.session, self.ns_name)

        game_mechanics._send_initial_game_state()

