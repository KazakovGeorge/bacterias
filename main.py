import pygame
import random
import os
import math
import sys

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
player_img = pygame.image.load(os.path.join(img_folder, 'p1.png'))


WIDTH = 1920
HEIGHT = 1080
FPS = 60

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / random.randint(1,10), HEIGHT / random.randint(1,10))
        self.speed = 2
        self.side = 0

    def walk_side(self):
        if(self.side > 360): self.side = self.side - 360
        if (self.side < 0): self.side = self.side + 360
        self.rect.x = self.rect.x + self.speed * math.cos(math.radians(self.side))
        self.rect.y = self.rect.y + self.speed * math.sin(math.radians(self.side))




    def walk(self):
        # Случайный выбор направления движения
        if random.randint(1, 2) == 1:
            walk_rand = random.randint(-10, 10)
            self.side += walk_rand
            #self.image = pygame.transform.rotate(self.image, walk_rand)
            #self.image.set_colorkey(WHITE)

        self.walk_side()

        # Проверка выхода за граниицы

        if self.rect.right > WIDTH: self.speed *= -1
        if self.rect.left < 0: self.speed *= -1
        if self.rect.bottom > HEIGHT: self.speed *= -1
        if self.rect.top < 0: self.speed *= -1
        """
        if self.rect.left > WIDTH: self.rect.right = 0
        if self.rect.right < 0: self.rect.left = WIDTH
        if self.rect.top > HEIGHT: self.rect.bottom = 0
        if self.rect.bottom < 0: self.rect.top = HEIGHT
        """

    def speed_random(self):
        if random.randint(0,100) == 1:
            self.speed += 1

    def update(self):
        self.walk()
        self.speed_random()


# Инициализация объектов
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group() # Группировка всех спрайтов

# Создание объектов мобов
player = Player()
all_sprites.add(player)


player2 = Player()
all_sprites.add(player2)

player3 = Player()
all_sprites.add(player3)

player4 = Player()
all_sprites.add(player4)


# Рабочий цикл

running =True
while running:
    clock.tick(FPS)

    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False


    # Обновление

    all_sprites.update()

    # Визуализация (сборка)

    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Переворот экрана
    pygame.display.flip()

    print(pygame.time.get_ticks()/1000, ' \\ ', player.rect.center)
    print(player.rect.center, " | ", player2.rect.center, " | ", player3.rect.center, " | ", player4.rect.center, " | ")
    print(player.speed, " | ", player2.speed, " | ", player3.speed, " | ", player4.speed, " | ", '\n')