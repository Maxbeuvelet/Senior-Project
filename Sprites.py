import pygame
from config import *
import math
import random


class SpriteSheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.surface([width, height])
        sprite.blit(self.sheet, (0,0), (x, y, width, height))  # selects cut out from loaded image


class Player(pygame.sprite.Sprite):  # pygame.sprite.Sprite a class in the pygame module to make it easy to make sprites
    def __init__(self, game, x, y):  # by passing in game we can access all variables in class Game
        self.game = game
        self._layer = PLAYER_LAYER  # By setting the layer it tells pygame which layer the sprites needs to be
        self.groups = self.game.all_sprites  # self.groups adds the player in the all sprites group
        pygame.sprite.Sprite.__init__(self, self.groups)  # call init method for the inherited class

        self.x = x * TILESIZE  # Player size in pixels
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'

        image_to_load = pygame.image.load("img/single.png")
        self.image = pygame.Surface([self.width, self.height])  # This is the image for the player class
        self.image.set_colorkey(BLACK)
        self.image.blit(image_to_load, (0,0))

        self.rect = self.image.get_rect()  # player hit box
        self.rect.x = self.x  # Tell pygame the coordinates
        self.rect.y = self.y

    def update(self):
        self.movement()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'


class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
