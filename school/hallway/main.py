import subprocess
import sys

from hamster import Hamster
from circle import Circle
from Sasha import sasha
from Bloomie import bloomie
from Thavel import thavel
from Grace import grace

import pygame as pg

pg.init()
screen = pg.display.set_mode((1500, 500))


all_sprites = pg.sprite.Group()
circle = Circle(1400, 300)
Sasha = sasha(1100, 310)
Bloomie = bloomie(800, 320)
Grace = grace(500, 250)
hamster = Hamster(100, 400)

all_sprites.add(hamster)
clock = pg.time.Clock()

# Загружаем фоны один раз
back_ground_img = pg.image.load('FPE.png').convert()
back_ground_img2 = pg.image.load('FPE.png').convert()
back_ground_img3 = pg.image.load('FPE.png').convert()
back_ground_img4 = pg.image.load('FPE2.png').convert()
back_ground_img5 = pg.image.load('FPE3.png').convert()

level = 0

run = True
while run:
    print(level)
    if level == 0 or level == 1:
        screen.blit(back_ground_img, (0, 0))
    elif level == 2 or level == 3:
        screen.blit(back_ground_img2, (0, 0))
    elif level == 4 or level == 5:
        screen.blit(back_ground_img3, (0, 0))
    elif level == 3:
        screen.blit(back_ground_img4, (0, 0))
    elif level == 4:
        screen.blit(back_ground_img5, (0, 0))
    elif level == 6:
        screen.blit(back_ground_img5, (0, 0))
    else:
        screen.fill('white')

    # Отрисовываем спрайты
    all_sprites.draw(screen)
    all_sprites.update()

    pg.display.update()

    # Обработка событий
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    # Логика смены уровней и запуск внешних скриптовd
    if level == 0:
        all_sprites.add(circle)

    if level == 1:
        circle.kill()
        all_sprites.add(Bloomie)
        pg.display.update()  # Обновляем экран с фоном и спрайтами перед запуском
        subprocess.run([sys.executable, "flappy_bird.py"])
        level += 1

    elif level == 3:
        Bloomie.kill()
        all_sprites.add(Sasha)
        pg.display.update()
        subprocess.run([sys.executable, "катя.py"])
        level += 1

    elif level == 5:
        Sasha.kill()
        all_sprites.add(Grace)
        pg.display.update()
        subprocess.run([sys.executable, "test.py"])
        level += 1

    elif level == 7:
        Grace.kill()
        pg.display.update()

    # Ограничения по движению hamster и смена уровней
    if hamster.rect.x > 1500:
        hamster.rect.x = 20
        level += 1

    if hamster.rect.x <= 20:
        hamster.rect.x = 20

    if hamster.rect.x >= 1400 and level == 7:
        hamster.rect.x = 1400

    clock.tick(60)

pg.quit()
