import pygame
from random import random, randint


pygame.init()


class Road(pygame.sprite.Sprite):
    def __init__(self, road_sprites, pictures):
        super().__init__(road_sprites)

        self.road_sprites = road_sprites

        self.image = pygame.Surface([600, 1000])
        self.image.fill((73, 77, 78))

        pygame.draw.rect(self.image, 'white', (10, 0, 10, 1000))
        pygame.draw.rect(self.image, 'white', (580, 0, 10, 1000))

        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 0

        self.create_tree = 0
        self.picture_tree = pictures[0]

        self.create_line = 0
        self.picture_line = pictures[1]

    def update(self):
        self.create_tree += 1
        self.create_line += 1
        t = randint(15, 35)
        if self.create_tree >= t:
            Tree(self.road_sprites, 50 + randint(-30, 30), self.picture_tree)
            Tree(self.road_sprites, 750 + randint(-30, 30), self.picture_tree)
            self.create_tree = 0
        if self.create_line == 5:
            Line(self.road_sprites, 300, self.picture_line)
            Line(self.road_sprites, 500, self.picture_line)
            self.create_line = 0


class Tree(pygame.sprite.Sprite):
    def __init__(self, road_sprites, x, img):
        super().__init__(road_sprites)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = -50
        self.speed = 20

    def update(self):
        self.rect = self.rect.move(0, self.speed)
        if self.rect.centery > 1000:
            self.kill()

    def get_speed(self, speed):
        self.speed = speed


class Line(pygame.sprite.Sprite):
    def __init__(self, road_sprites, x1, img1):
        super().__init__(road_sprites)
        self.image = img1
        self.rect = self.image.get_rect()
        self.rect.centerx = x1
        self.rect.centery = -100
        self.speed = 20

    def update(self):
        self.rect = self.rect.move(0, self.speed)
        if self.rect.centery > 1000:
            self.kill()

    def get_speed(self, speed):
        self.speed = speed
