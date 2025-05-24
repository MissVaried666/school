import pygame as pg

pg.init()
pg.font.init()

screen = pg.display.set_mode((1500, 500))

font = pg.font.SysFont("None", 100)

W, H = 600, 600

score = 0
level = 1

text_input = ""
input_active = True

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            input_active = True
            text_input = ""
        elif event.type == pg.KEYDOWN and input_active:
            if event.key == pg.K_RETURN:
                input_active = False
            elif event.key == pg.K_BACKSPACE:
                text_input = text_input[:-1]
            else:
                text_input += event.unicode

    if level == 1:
        text = font.render(f"Реши уравнение:", False, "white")
        screen.blit(text, (W // 2 - 65, 100))

        text = font.render(f"х-3х(1-12х)=11-(5-6х)(6х+5)", False, "white")
        screen.blit(text, (W // 2 - 65, 200))

        if text_input == "7" and input_active == False:
            print("Правильнo")
            screen.fill("black")
            text = font.render(f"Правильно", False, "white")
            screen.blit(text, (W // 2 - 65, 300))
        elif text_input != "7" and input_active == False and len(text_input) > 0:
            run = False

    text_surf = font.render(text_input, True, (255, 0, 0))
    screen.blit(text_surf, (W // 2 - 65, 400))

    pg.display.update()

pg.quit()
