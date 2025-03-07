from abc import ABC, abstractmethod
from domain.game_session import GameSession


class IGameView(ABC):
    @abstractmethod
    def display_start_screen(self):
        """
        Отображает стартовый экран игры.
        """
        pass

    @abstractmethod
    def update_view(self, game_session: GameSession):
        """
        Обновляет отображение игры в соответствии с текущим состоянием.
        """
        pass

    @abstractmethod
    def display_game_over(self):
        """
        Отображает экран окончания игры.
        """
        pass

    @abstractmethod
    def display_winner(self):
        """
        Отображает экран победы.
        """
        pass
