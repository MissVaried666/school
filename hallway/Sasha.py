import pygame as pg


class sasha(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('MissSasha.png')
        self.rect = self.image.get_rect(center=(x, y))