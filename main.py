from controller.game_controller import GameController

from presentation.cli.game_view import GameView
from presentation.cli.ui import UI

from icecream import ic

# ic.configureOutput(outputFunction=lambda _: None)

def main() -> int:
    game_controller = GameController(GameView(), UI())
    game_controller.start_game()

    return 0


if __name__ == "__main__":
    main()
