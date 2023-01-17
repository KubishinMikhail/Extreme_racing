import pygame
from random import randint


pygame.init()


class Road(pygame.sprite.Sprite):
    def __init__(self, road_sprites, pictures, cars_pictures, speed):
        super().__init__(road_sprites)

        self.road_sprites = road_sprites

        self.image = pygame.Surface([600, 1000])
        self.image.fill((73, 77, 78))

        pygame.draw.rect(self.image, 'white', (10, 0, 10, 1000))
        pygame.draw.rect(self.image, 'white', (580, 0, 10, 1000))
        self.speed = speed

        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 0

        self.create_tree = 0
        self.picture_tree = pictures[0]

        self.create_line = 0
        self.picture_line = pictures[1]

        self.create_cars = 0
        self.cars_pictures = cars_pictures

        self.cars_positions = [200, 400, 600]

        self.create_fuel = 0
        self. picture_fuel = pictures[2]

        self.fuel_pos = [200, 400, 600]

    def update(self):
        self.create_tree += 1
        self.create_line += 1
        self.create_fuel += 1
        self.create_cars += 1
        t = randint(15, 35)
        if self.create_tree >= t:
            Tree(self.road_sprites, 50 + randint(-30, 30), self.picture_tree, self.speed)
            Tree(self.road_sprites, 750 + randint(-30, 30), self.picture_tree, self.speed)
            self.create_tree = 0
        if self.create_line == 5:
            Line(self.road_sprites, 300, self.picture_line, self.speed)
            Line(self.road_sprites, 500, self.picture_line, self.speed)
            self.create_line = 0
        if self.create_cars == 100:
            Cars(self.road_sprites, self.cars_positions[randint(0, 2)], self.cars_pictures[randint(0, 3)])
            self.create_cars = 0
        if self.speed == 10:
            if self.create_line == 20:
                Line(self.road_sprites, 300, self.picture_line, self.speed)
                Line(self.road_sprites, 500, self.picture_line, self.speed)
                self.create_line = 0
        if self.speed == 15:
            if self.create_line == 15:
                Line(self.road_sprites, 300, self.picture_line, self.speed)
                Line(self.road_sprites, 500, self.picture_line, self.speed)
                self.create_line = 0
        if self.speed == 20:
            if self.create_line == 10:
                Line(self.road_sprites, 300, self.picture_line, self.speed)
                Line(self.road_sprites, 500, self.picture_line, self.speed)
                self.create_line = 0
        if self.create_fuel == 1000: # пикселях
            Fuel(self.road_sprites, self.fuel_pos[randint(0, 2)], self.picture_fuel, self.speed)
            self.create_fuel = 0

    def up_speed(self):
        if self.speed < 20:
            self.speed += 5
        else:
            self.speed = 20

    def down_speed(self):
        if self.speed > 10:
            self.speed -= 5
        else:
            self.speed = 10


class Tree(pygame.sprite.Sprite):
    def __init__(self, road_sprites, x, img, speed):
        super().__init__(road_sprites)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = -50
        self.speed = speed

    def update(self):
        self.rect = self.rect.move(0, self.speed)
        if self.rect.centery > 1000:
            self.kill()

    def get_speed(self, speed):
        self.speed = speed


class Line(pygame.sprite.Sprite):
    def __init__(self, road_sprites, x1, img1, speed):
        super().__init__(road_sprites)
        self.image = img1
        self.rect = self.image.get_rect()
        self.rect.centerx = x1
        self.rect.centery = -100
        self.speed = speed

    def update(self):
        self.rect = self.rect.move(0, self.speed)
        if self.rect.centery > 1200:
            self.kill()

    def get_speed(self, speed):
        self.speed = speed


class Fuel(pygame.sprite.Sprite):
    def __init__(self, road_sprites, x3, img3, speed):
        super().__init__(road_sprites)
        self.image = img3
        self.rect = self.image.get_rect()
        self.rect.centerx = x3
        self.rect.centery = -50
        self.speed = 20

    def update(self):
        self.rect = self.rect.move(0, self.speed)
        if self.rect.centery > 1000:
            self.kill()

    def get_speed(self, speed):
        self.speed = 1


class Cars(pygame.sprite.Sprite):
    def __init__(self, road_sprites, x2, car_img):
        super().__init__(road_sprites)
        self.image = car_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x2
        self.rect.centery = -100
        self.speed = 20

    def update(self):
        self.rect = self.rect.move(0, self.speed)
        if self.rect.centery > 1100:
            self.kill()

    def get_speed(self, speed):
        self.speed = randint(3, 5)
