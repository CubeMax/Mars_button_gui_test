import os

import arcade
from arcade.gui import UIManager

from gui.buttons.button import ButtonAction
from gui.buttons.layout_manager import LayoutManager
from gui.buttons.button import ButtonType


class Menu(arcade.View):
    def __init__(self, grid_width: int, grid_height: int):
        super().__init__()
        arcade.set_background_color(arcade.color.BLACK)
        background_path = os.path.join(arcade.get_window().MAIN_PATH, "ress", "wallpaper", "Mars.jpg")
        self.background = arcade.load_texture(background_path, hit_box_algorithm="None")
        self.ui_manager = UIManager()
        self.layout_manager = LayoutManager(self.window.width, self.window.height, grid_width, grid_height)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def setup(self):
        pass

    def draw_background(self):
        screen_width, screen_height = self.window.get_size()
        background_width, background_height = self.background.width, self.background.height
        scale = screen_height / background_height
        arcade.draw_scaled_texture_rectangle(screen_width // 2, screen_height // 2, self.background, scale)

    def on_draw(self):
        arcade.start_render()
        self.draw_background()

    def on_resize(self, width, height):
        self.layout_manager.on_resize(width, height)


class StartMenu(Menu):
    def __init__(self):
        super().__init__(3, 5)

        win = arcade.get_window()

        def command(button_type: ButtonType):
            if button_type == ButtonType.SINGLE_PLAYER:
                win.setup_game()
            elif button_type == ButtonType.MULTIPLAYER:
                win.setup_game()
            elif button_type == ButtonType.SETTINGS:
                win.show_view(win.MENU_SETTINGS)
                win.MENU_SETTINGS.setup()

        self.button_singleplayer = ButtonAction("Singleplayer", ButtonType.SINGLE_PLAYER, command)
        self.button_multiplayer = ButtonAction("Multiplayer", ButtonType.MULTIPLAYER, command)
        self.button_settings = ButtonAction("Settings", ButtonType.SETTINGS, command)

    def setup(self):
        self.ui_manager.purge_ui_elements()
        self.layout_manager.clear()

        self.layout_manager.add(self.button_singleplayer, 2, 4)
        self.layout_manager.add(self.button_multiplayer, 2, 3)
        self.layout_manager.add(self.button_settings, 2, 2)
        for button in self.layout_manager:
            self.ui_manager.add_ui_element(button)


class MenuSettings(Menu):
    def __init__(self):
        super().__init__(7, 7)

        win = arcade.get_window()

        def command(button_type: ButtonType):
            if button_type == ButtonType.BACK:
                win.START_MENU.setup()
                win.show_view(win.START_MENU)
            elif button_type == ButtonType.START:
                win.setup_game()

        self.button_start = ButtonAction("Start\ngame", ButtonType.START, command)
        self.button_back = ButtonAction("back", ButtonType.BACK, command)

    def setup(self):
        self.ui_manager.purge_ui_elements()
        self.layout_manager.clear()

        self.layout_manager.add(self.button_start, 4, 1)
        self.layout_manager.add(self.button_back, 1, 1)

        for button in self.layout_manager:
            self.ui_manager.add_ui_element(button)
