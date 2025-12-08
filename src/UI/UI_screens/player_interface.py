from src.UI.UI_screens.UI import UI
from src.UI.UI_screens.status_bar import StatusBar
from src.UI.UI_components.UI_componenets import *

class PlayerInterface(UI):
    def __init__(self, game, player):
        super().__init__(game, x_p=0, y_p=0, width_p=1, height_p=1)
        self.player = player

        self.sanity_bar = StatusBar(game, x_p=0.104, y_p=0.02, width_p=0.2, height_p=0.03, outline_color=(100, 100, 100, 25), bar_color=(125, 125, 0, 25))
        self.battery_bar = StatusBar(game, x_p=0.104, y_p=0.06, width_p=0.2, height_p=0.03, outline_color=(100, 100, 100, 25), bar_color=(0, 125, 125, 25))
        
        self.flashlight = UIImage(
            x_p=1,
            y_p=1,
            width_p=0.3,
            height_p=0.45,
            image=game.image_manager.get_image("flashlight")
        )

        self.root_panel.add_children([self.sanity_bar.root_panel, self.battery_bar.root_panel, self.flashlight])

    def _update(self):
        super()._update()
        self.sanity_bar.update_bar(self.player.sanity / self.player.max_sanity)
        self.battery_bar.update_bar(self.player.battery / self.player.max_battery)