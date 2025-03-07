from ..igame_view import IGameView

class GameView(IGameView):
    def display_start_screen(self):
        """
        Отображает стартовый экран игры.
        """
        pass


    def update_view(self, game_session: "GameSession"):
        """
        Обновляет отображение игры в соответствии с текущим состоянием.
        """
        pass

    def display_game_over(self):
        """
        Отображает экран окончания игры.
        """
        pass

    def display_winner(self):
        """
        Отображает экран победы.
        """
        pass