
# list of all the buttons
class LayoutManager(list):
    def __init__(self, screen_width, screen_height, grid_width, grid_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.grid_width = grid_width
        self.grid_height = grid_height

    def on_resize(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        for button in self:
            button.resize(screen_width, screen_height)

    def add(self, button, grid_x: int, grid_y: int):
        self.append(button)

        button.grid_x = grid_x
        button.grid_y = grid_y
        button.grid_width = self.grid_width
        button.grid_height = self.grid_height

        button.resize(self.screen_width, self.screen_height)
