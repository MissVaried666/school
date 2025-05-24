import pygame as pg


class Circle(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('Msemily.png')
        self.rect = self.image.get_rect(center=(x, y))
