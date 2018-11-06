# file created by Charlie Fezell
# sprite classes for game

import pygame as pg
from pygame.sprite import Sprite
import random
from settings import *

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((30,40))
        self.image.fill(BLUEISH)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.vx = 0
        self.vy = 0
    def update(self):
        self.vx = 0
        self.vy = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vx = -10
        if keys[pg.K_RIGHT]:
            self.vx = 10
        if keys[pg.K_UP]:
            self.vy = -10
        if keys[pg.K_DOWN]:
            self.vy = 10
        
        self.rect.x += self.vx
        self.rect.y += self.vy