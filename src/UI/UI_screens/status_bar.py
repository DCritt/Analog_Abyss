from src.UI.UI_screens.UI import UI
from src.UI.UI_components.UI_componenets import *

class StatusBar(UI):
    def __init__(self, game, x_p, y_p, width_p, height_p, outline_color, bar_color):
        super().__init__(game, x_p, y_p, width_p, height_p)

        self.outline = UIColorImage(
            x_p=0,
            y_p=0,
            width_p=1,
            height_p=1,
            color=outline_color,
            outline_width=3
        )
        self.bar = UIColorImage(
            x_p=0,
            y_p=0,
            width_p=1,
            height_p=1,
            color=bar_color
        )

        self.root_panel.add_children([self.bar, self.outline])

    def update_bar(self, bar_portion):
        self.bar.resize(bar_portion, 1)
