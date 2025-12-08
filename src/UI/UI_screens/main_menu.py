from src.UI.UI_screens.UI import UI
from src.UI.UI_builders.main_menu_panel import build_main_menu_panel
from src.UI.UI_builders.settings_panel import build_settings_panel

class MainMenu(UI):
    def __init__(self, game):
        super().__init__(game, x_p=0, y_p=0, width_p=1, height_p=1)

        self.menu_panel = build_main_menu_panel(game, self._toggle_settings)
        self.settings_panel = build_settings_panel(self._toggle_settings)

        self.root_panel.add_children([self.menu_panel, self.settings_panel])

    def _toggle_settings(self):
        self.settings_panel.active = not self.settings_panel.active
        self.menu_panel.active = not self.menu_panel.active