import pygame
import controls
from tank import Tank
from pygame.sprite import Group
from stats import Stats
from scores import Scores



def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Космические защитники")
    bg_color=(0, 0, 0)
    tank = Tank(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, tank, bullets)
        if stats.run_game:
            tank.update_tank()
            controls.update(bg_color, screen, stats, sc, tank, inos, bullets)
            controls.update_bullets(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen, sc, tank, inos, bullets)


run()