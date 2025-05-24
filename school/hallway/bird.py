import pygame as pg

pg.mixer.init()



class Bird(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('hamster.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.vector = 2
        self.jump_time = None

    def jump(self):
        self.vector = -5
        self.jump_time = pg.time.get_ticks()


    def update(self):

        self.rect.y += self.vector
        if self.rect.bottom > 600:
            self.rect.bottom = 600

        if self.rect.top < 0:
            self.rect.top = 0

        if self.jump_time is not None:
            elapsed_time = pg.time.get_ticks() - self.jump_time
            if elapsed_time >= 300:
                self.vector = 2
