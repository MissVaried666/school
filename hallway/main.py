import pygame as pg

from hamster import Hamster

from circle import Circle

from Sasha import sasha

from Bloomie import bloomie

from Thavel import thavel

from Grace import grace

from flappy_folder.flappy_bird import *

pg.init()
screen = pg.display.set_mode((1500, 500))

circle = Circle(1400, 300)
all_sprites = pg.sprite.Group(circle)

Sasha = sasha(1100, 310)

Bloomie = bloomie(800,320)

Thavel = thavel(1400,400)

Grace = grace(500,250)

hamster = Hamster(100, 400)

all_sprites.add(hamster)
clock = pg.time.Clock()


clock = pg.time.Clock()

back_ground_img = pg.image.load('FPE.png')
back_gorund = pg.surface.Surface((back_ground_img.get_width(), back_ground_img.get_height()))

back_ground_img2 = pg.image.load('FPE.png')

back_ground_img3 = pg.image.load('FPE.png')

back_ground_img4 = pg.image.load('FPE2.png')

back_ground_img5 = pg.image.load('FPE3.png')

level = 0

run = True
while run:
    screen.fill('white')
    if level == 0:
        back_gorund.blit(back_ground_img, (0, 0))
        screen.blit(back_gorund, (0, 0))

    if level == 1:
        flappy_bird()
        circle.kill()
        all_sprites.add(Bloomie)
        back_gorund.blit(back_ground_img2, (0, 0))
        screen.blit(back_gorund, (0, 0))
    if level == 2:
        all_sprites.add(Sasha)
        Bloomie.kill()
        back_gorund.blit(back_ground_img3, (0,0))
        screen.blit(back_gorund, (0, 0))
    if level == 3:
        Sasha.kill()
        all_sprites.add(Thavel)
        back_gorund.blit(back_ground_img4, (0, 0))
        screen.blit(back_gorund, (0, 0))
    if level == 4:
        Thavel.kill()
        all_sprites.add(Grace)
        back_gorund.blit(back_ground_img5, (0, 0))
        screen.blit(back_gorund, (0, 0))

    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    if hamster.rect.x > 1500:
        hamster.rect.x = 20
        level += 1

    if hamster.rect.x <= 20:
        hamster.rect.x = 20

    if hamster.rect.x >= 1400 and level == 4:
        hamster.rect.x = 1400

    all_sprites.draw(screen)
    all_sprites.update()
    pg.display.update()




pg.quit()
