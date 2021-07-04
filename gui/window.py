import arcade

from gui.screens.start_menu import StartMenu, MenuSettings


class Window(arcade.Window):

    def __init__(self, width, height, title, main_path):
        super().__init__(width, height, title, resizable=True)
        self.MAIN_PATH = main_path

        self.START_MENU = StartMenu()
        self.START_MENU.setup()

        self.MENU_SETTINGS = MenuSettings()

    def setup_game(self):
        # create the game
        pass

    def on_resize(self, width, height):
        super().on_resize(width, height)
        # print(f"Window resized to: {width}, {height}")

