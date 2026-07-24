import pygame.font
from tank import Tank
from pygame.sprite import Group

class Scores():
    #Вывод игровой информации#
    def __init__(self, screen, stats):
        #Инициализируем подсчёт очков#
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_hight_score()
        self.image_tanks()

    def image_score(self):
        #Преобразовывает текст счёта в графическое изображение#
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_hight_score(self):
        #Преобразует рекорд в графическое изображение#
        self.hight_score_image = self.font.render(str(self.stats.hight_score), True, self.text_color, (0, 0, 0))
        self.hight_score_rect = self.hight_score_image.get_rect()
        self.hight_score_rect.centerx = self.screen_rect.centerx
        self.hight_score_rect.top = self.screen_rect.top + 20

    def image_tanks(self):
        #Количество жизней#
        self.tanks = Group()
        for tank_number in range(self.stats.tanks_left):
            tank = Tank(self.screen)
            tank.rect.x = 15 + tank_number * tank.rect.width
            tank.rect.y = 20
            self.tanks.add(tank)


    def show_score(self):
        #вывод счёта на экран#
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.hight_score_image, self.hight_score_rect)
        self.tanks.draw(self.screen)
        