import pygame as pg
pg.init()
pg.display.set_mode((1500,500))

run=True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run=False

pg.quit()