import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, tank):
        #Создаём пулю в позиции пушки#
        super(Bullet, self). __init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 10, 15)
        self.color = 255, 255, 255
        self.speed = 4.5
        self.rect.centerx = tank.rect.centerx
        self.rect.top = tank.rect.top
        self.y = float(self.rect.y)

    def update(self):
        #Перемещение пули вверх#
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        #Рисуем пулю на экране#
        pygame.draw.rect(self.screen, self.color, self.rect)
    

       