from presentation.igame_view import IGameView
from presentation.iui import IUI
from domain.game_session import GameSession


class GameController:
    game_view: IGameView
    ui: IUI
    game_session: GameSession | None = None

    def __init__(self, game_view: IGameView, ui: IUI):
        self.game_view = game_view
        self.ui = ui

    def start_game(self):
        # self.model = Model()
        # self.mode.start_game()

        self.game_session = GameSession()
        self.game_session.level.generate_level()
        # self.game_view.display_start_screen()

        # while self.game_session.is_active():
        # action = self.ui.get_user_input()
        # self.process_action(action)
        # self.game_view.update_view(self.game_session)
        pass

    def process_action(self, action):
        # Логика обработки действий игрока
        pass
