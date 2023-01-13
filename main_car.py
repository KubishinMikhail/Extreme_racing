import pygame

pygame.init()
rotates = [pygame.image.load('pictures/main_car.png'),
           pygame.image.load('pictures/main_car_rotate_1.png'),
           pygame.image.load('pictures/main_car_rotate_2.png'),
           pygame.image.load('pictures/main_car_rotate_3.png'),
           pygame.image.load('pictures/main_car_rotate_4.png')]
main_car = rotates[0]


class MainCar(pygame.sprite.Sprite):
    def __init__(self, pos, sprite_of_car):
        super().__init__(sprite_of_car)
        self.image = main_car
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.position_of_car = pos[0]
        self.rect.centerx = self.position_of_car   # 200, 400, 600
        self.rect.y = pos[1]
        self.run_left = False
        self.run_right = False
        self.car_rotate = False

    def update(self, position, count_of_frames_2):
        if self.run_left:
            if not self.car_rotate:
                self.position_of_car -= 200
            self.car_rotate = True
            if count_of_frames_2 < 5:
                self.image = rotates[1]
            elif 5 <= count_of_frames_2 < 10:
                self.image = rotates[2]
            elif 35 <= count_of_frames_2 < 40:
                self.image = rotates[1]
            elif count_of_frames_2 == 40:
                self.image = rotates[0]
                self.rect.centerx = self.position_of_car
                self.run_left = False
                self.car_rotate = False
            self.rect = self.rect.move(-5, 0)
        if self.run_right:
            if not self.car_rotate:
                self.position_of_car += 200
            self.car_rotate = True
            if count_of_frames_2 < 5:
                self.image = rotates[3]
            elif 5 <= count_of_frames_2 < 10:
                self.image = rotates[4]
            elif 35 <= count_of_frames_2 < 40:
                self.image = rotates[3]
            elif count_of_frames_2 == 40:
                self.image = rotates[0]
                self.rect.centerx = self.position_of_car
                self.run_right = False
                self.car_rotate = False
            self.rect = self.rect.move(5, 0)
