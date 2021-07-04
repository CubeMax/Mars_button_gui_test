
from enum import Enum

import arcade
from arcade.gui import UIGhostFlatButton

BORDER_WIDTH = 3
SPACE_BETWEEN_BUTTONS = 0.2
COLOR_TRANSPARENT = arcade.make_transparent_color((0, 0, 0), 0)


class ButtonType(Enum):
    START = "Start"
    BACK = "Back"

    SINGLE_PLAYER = "SinglePlayer"
    MULTIPLAYER = "Multiplayer"
    LOAD_GAME = "LoadGame"
    SETTINGS = "Settings"


class ButtonAction(UIGhostFlatButton):
    def __init__(self, name, button_type: ButtonType, command):
        super().__init__(name)
        self.name = name
        self.button_type = button_type
        self.command = command
        self.grid_width = None
        self.grid_height = None
        self.grid_x = None
        self.grid_y = None
        self.font_size = None
        self.set_style_attrs(font_size=20,
                             font="Kenney Blocks Font",
                             font_color=arcade.color.YELLOW,
                             font_color_hover=arcade.color.YELLOW,
                             font_color_press=arcade.color.YELLOW,
                             bg_color=COLOR_TRANSPARENT,
                             bg_color_hover=COLOR_TRANSPARENT,
                             bg_color_press=COLOR_TRANSPARENT,
                             border_color=arcade.color.YELLOW,
                             border_color_hover=arcade.color.YELLOW,
                             border_color_press=arcade.color.YELLOW,
                             border_width=BORDER_WIDTH)

    def resize(self, screen_width, screen_height):
        self.center_x = screen_width * self.grid_x // (self.grid_width + 1)
        self.center_y = screen_height * self.grid_y // (self.grid_height + 1)

        # screen_i = button_i * grid_i * (1 + 2 * SPACE)
        self.width = int(screen_width / (self.grid_width * (1 + 2 * SPACE_BETWEEN_BUTTONS)))
        self.height = int(screen_height / (self.grid_height * (1 + 2 * SPACE_BETWEEN_BUTTONS)))

        self.font_size = self.width // 10
        self.set_style_attrs(font_size=self.font_size)

    def on_click(self):
        self.command(self.button_type)
