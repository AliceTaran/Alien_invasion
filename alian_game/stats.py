import pygame
import os 

class Stats():
    #Отслеживание статистики#

    def __init__(self):
        #Инициализирует статистику#
        self.reset_stats()
        self.run_game = True
        current_dir = os.path.dirname(__file__)
        records_path = os.path.join(current_dir, 'hightscore.txt')
        
        # Читаем рекорд или создаем файл, если его нет
        try:
            with open(records_path, 'r') as f:
                self.hight_score = int(f.readline().strip())
        except (FileNotFoundError, ValueError):
            # Если файла нет или он пустой, создаем со значением 0
            self.hight_score = 0
            with open(records_path, 'w') as f:
                f.write('0')

    def reset_stats(self):
        #статистика изменяющаяся во время игры#
        self.tanks_left = 2
        self.score = 0