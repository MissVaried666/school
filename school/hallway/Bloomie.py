import pygame as pg


class bloomie(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('missbloome11.png')
        self.rect = self.image.get_rect(center=(x, y))