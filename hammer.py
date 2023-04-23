import pygame
import random


class Hammer():
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('hammer.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        # self.rect = self.image.get_rect()

        # self.rect.midbottom = self.screen_rect.midbottom

        self.VRX = 200
        self.VRY = 200
        self.x = int(self.screen_rect.width * self.VRX / 255)
        self.y = int(self.screen_rect.height * self.VRY / 255)

        self.position = (self.x, self.y)

    def blitme(self):
        self.screen.blit(self.image, self.position)

    def update(self):
        # 树莓派上改用adc读取
        self.VRX = 200
        self.VRY = 200
        self.x = int(self.screen_rect.width * self.VRX / 255)
        self.y = int(self.screen_rect.height * self.VRY / 255)
        self.position = (self.x, self.y)
