import pygame, sys
from bullet import Bullet
from ino import Ino
import time

def events(screen, tank, bullets):
     for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                #Вправо#
                if event.key == pygame.K_d:
                      tank.mright = True
                elif event.key == pygame.K_a:
                      tank.mleft = True
                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(screen,tank) 
                    bullets.add(new_bullet)
            elif event.type == pygame.KEYUP:
                #Вправо#
                if event.key == pygame.K_d:
                      tank.mright = False
                elif event.key == pygame.K_a:
                      tank.mleft = False

def update(bg_color, screen, stats, sc, tank, inos, bullets):
     #Обновление экрана#
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    tank.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, sc, inos, bullets):
    #Обновлять позиции пуль#
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        for inos in collisions.values():
            stats.score +=10 * len(inos)
        sc.image_score()
        check_hight_score(stats, sc)
        sc.image_tanks()
    if len(inos) ==0:
        bullets.empty()
        create_army(screen, inos)

def tank_kill(stats, screen, sc, tank, inos, bullets):
    #столкновение пушки и армии#
    if stats.tanks_left > 0:
        stats.tanks_left -= 1
        sc.image_tanks()
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        tank.create_tank()
        time.sleep(2)
    else:
        stats.run_game = False
        sys.exit()

def update_inos(stats, screen, sc, tank, inos, bullets):
    #обновляет позицию пришельцев#
    inos.update()
    if pygame.sprite.spritecollideany(tank, inos,):
        tank_kill(stats, screen, sc,tank, inos, bullets)
    inos_check(stats, screen, sc, tank, inos, bullets)

def inos_check(stats, screen, sc, tank, inos, bullets):
    #Проверка, добралась ли армия до края экрана#
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            tank_kill(stats, screen, sc, tank, inos, bullets)
            break


def create_army(screen, inos):
    #Создание армии пришельцев#
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((600 - 200 - 2 * ino_height) / ino_height)



    for row_number in range(number_ino_y -1):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + (ino_width * ino_number)
            ino.y = ino_height + (ino_height * row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + (ino.rect.height * row_number)
            inos.add(ino)
    

def check_hight_score(stats, sc):
    #Проверка новых рекордов#
    if stats.score > stats.hight_score:
        stats.hight_score = stats.score
        sc.image_hight_score()
        with open('hightscore.txt', 'w') as f:
            f.write(str(stats.hight_score))
