import pygame

from main_car import MainCar
from road import Road
import random


pygame.init()
sprite_of_car = pygame.sprite.GroupSingle()
road_sprites = pygame.sprite.Group()
rotates = [pygame.image.load('pictures/main_car.png'),
           pygame.image.load('pictures/main_car_rotate_1.png'),
           pygame.image.load('pictures/main_car_rotate_2.png'),
           pygame.image.load('pictures/main_car_rotate_3.png'),
           pygame.image.load('pictures/main_car_rotate_4.png')]

pictures = [pygame.image.load('pictures/tree.png'),
            pygame.image.load('pictures/line.png')]

cars_pictures = [pygame.image.load('pictures/car_1.png'),
                 pygame.image.load('pictures/car_2.png'),
                 pygame.image.load('pictures/car_3.png'),
                 pygame.image.load('pictures/car_4.png')]


if __name__ == '__main__':
    size = width, height = 800, 1000
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Extreme racing')

    fps = 60
    clock = pygame.time.Clock()

    road = Road(road_sprites, pictures, cars_pictures)
    car = MainCar((400, 500), sprite_of_car)

    running = False
    pos = True
    count_of_frames = 0
    image = pygame.image.load('pictures/start1.png')
    xs, ys = 0, 0

    while not running:
        screen.fill('white')
        screen.blit(image, (xs, ys))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                while ys < 1000:
                    ys += 10
                    screen.blit(image, (xs, ys))
                    pygame.display.flip()
                running = True
                break
        pygame.display.flip()
        clock.tick(fps)

    while running:
        screen.fill((95, 169, 42))
        if count_of_frames:
            count_of_frames += 1
            sprite_of_car.update(pos, count_of_frames)
            if count_of_frames == 41:
                count_of_frames = 0
        # screen.blit(road, (0, 0))
        # sprite_of_car.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.KEYUP and not count_of_frames:
                pos = event.key
                count_of_frames = 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                if car.position_of_car != 200 and not car.car_rotate:
                    car.run_left = True
                    car.run_right = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                if car.position_of_car != 600 and not car.car_rotate:
                    car.run_left = False
                    car.run_right = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                if road.speed < 15:
                    road.speed += 5
                else:
                    road.speed = 15
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                if road.speed > 5:
                    road.speed -= 5
                else:
                    road.speed = 5

        road_sprites.update()
        road_sprites.draw(screen)
        sprite_of_car.draw(screen)

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
