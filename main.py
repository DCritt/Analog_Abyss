import pygame
from settings import RESOLUTION, FPS
from map_arrays import *
from map import *
from player import Player
from player_camera import PlayerCamera
from multiprocessing import Pool, cpu_count
from pool import worker_init

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.running = True

        self.map = Map(self, map1)
        self.player = Player(self)
        self.player_camera = PlayerCamera(self, self.player)

    def set_pool(self, pool):
        self.pool = pool

    def update(self):
        self.player.update()
        pygame.display.update()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')


    def draw(self):
        self.screen.fill((0, 0, 0))
        #self.map.draw()
        #self.player.draw()
        #pygame.draw.rect(self.screen, (125, 125, 125), (0, HEIGHT // 2, WIDTH, HEIGHT // 2))
        self.player_camera.ray_cast()
        

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        while self.running:
            self.check_events()
            self.draw()
            self.update()

        pygame.quit()

if __name__ == '__main__':
        game = Game()
        with Pool(cpu_count(), worker_init, (game.map.map_dic,)) as pool:
            game.set_pool(pool)
            game.run()
    