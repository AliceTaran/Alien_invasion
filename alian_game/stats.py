import pygame
class Stats():
    #Отслеживание статистики#

    def __init__(self):
        #Инициализирует статистику#
        self.reset_stats()
        self.run_game = True
        with open('hightscore.txt', 'r') as f:
            self.hight_score = int(f.readline())

    def reset_stats(self):
        #статистика изменяющаяся во время игры#
        self.tanks_left = 2
        self.score = 0