import pygame as pg

class hamster(pg.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pg.image.load('сюда вставить рисунок,Варя')
        self.rect=self.image.get_rect(center=(x,y))
        self.vector=3
