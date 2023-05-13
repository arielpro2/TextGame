from TextGame.GameEngine.level_loader import LevelLoader

MAIN_MENU_PROMPT = """
Welcome to TextGame!

Please choose an option:

1) Start Game.
2) Quit. 

"""


class Engine:
    def __init__(self):
        self.level_loader = LevelLoader()

    def main_menu(self):
        while True:
            print(MAIN_MENU_PROMPT)
            choice = input()

            if choice == 1:
                self.start_game()

            if choice == 2:
                break

    def start_game(self):
        pass

    pass
