import pygame
import random, os, math
import config, objects

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
player_img = pygame.image.load(os.path.join(img_folder, 'p1.png'))


class Bacteria(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(config.WHITE)

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, config.WIDTH - 50), random.randint(50, config.HEIGHT - 50))

        self.speed = 2
        self.side = 0
        self.hp = 100

    #   Идти прямо по направлению
    def walk_side(self):
        if(self.side > 360): self.side = self.side - 360
        if(self.side < 0): self.side = self.side + 360
        self.rect.x = self.rect.x + self.speed * math.cos(math.radians(self.side))
        self.rect.y = self.rect.y + self.speed * math.sin(math.radians(self.side))

    def walk(self):
        # Случайный выбор направления движения
        if random.randint(1, 2) == 1:
            walk_rand = random.randint(-20, 20)
            self.side += walk_rand
        self.walk_side()
        # Проверка выхода за граниицы
        if self.rect.right > config.WIDTH:
            self.speed *= -1
        if self.rect.left < 0:
            self.speed *= -1

        if self.rect.bottom > config.HEIGHT:
            self.speed *= -1
        if self.rect.top < 0:
            self.speed *= -1

    def check_colision(self):
        for sprite in objects.all_sprites:
            if (sprite.__module__ == Bacteria().__module__) and (sprite != self):
                if self.rect.colliderect(sprite):
                    self.hp -= random.randint(0,5)
                    self.speed *= -1
                    self.walk_side()

    def check_health(self):
        if self.hp <= 0:
            self.kill()

    def update(self):
        self.walk()
        self.check_colision()
        self.check_health()

