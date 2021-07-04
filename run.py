#!/usr/bin/env python3

import os

import arcade

from gui.window import Window

SCREEN_WIDTH = 1024 * 3 // 2
SCREEN_HEIGHT = 512 * 3 // 2
SCREEN_TITLE = "Mars"
FPS = 60

# main path to all ressource and source files
PATH_TO_RUN = os.getcwd()


def main():
    main_windows = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, PATH_TO_RUN)
    main_windows.set_update_rate(1 / FPS)
    main_windows.show_view(main_windows.START_MENU)
    arcade.run()


if __name__ == "__main__":
    main()
