import os

import pygame
import config
from objects import all_sprites
from bacteria_class import Bacteria


# Инициализация объектов
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()

# Создание объектов мобов
for i in range(config.numbersOfBacterias):
    all_sprites.add(Bacteria())


# Рабочий цикл

running = True
while running:
    clock.tick(config.FPS)

    print(f'Bacterias: {len(all_sprites)}')

    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()

    # Визуализация (сборка)
    screen.fill(config.BLACK)
    all_sprites.draw(screen)

    # Переворот экрана
    pygame.display.flip()

    os.system('cls')