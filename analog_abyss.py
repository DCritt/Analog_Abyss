import pygame

pygame.init()

#Screen Setup
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("analog_abyss")

#Game loop
running = True

while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

#Game logic


pygame.quit()