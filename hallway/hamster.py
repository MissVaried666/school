import pygame as pg


class Hamster(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('hamster.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.vector = 7

    def update(self):
        key = pg.key.get_pressed()

        if key[pg.K_a]:
            self.rect.x -= self.vector
        if key[pg.K_d]:
            self.rect.x += self.vector

