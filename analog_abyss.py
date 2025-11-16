from src.game_management.game_manager import GameManager
from src.game_management.scene import UIScene, LevelScene
from src.data.map_arrays import map1

if __name__ == '__main__':
    game = GameManager()
    game.load_scene(UIScene(game, None))
    game.run()