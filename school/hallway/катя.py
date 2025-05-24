import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((1500, 500))
clock = pg.time.Clock()
font = pg.font.SysFont(None, 48)

# Определяем квадраты и их цвета
red = pg.Rect(100, 100, 300, 300)
blue = pg.Rect(600, 100, 300, 300)
green = pg.Rect(1100, 100, 300, 300)
colors = {
    1: ((255, 0, 0), red),
    2: ((0, 0, 255), blue),
    3: ((0, 255, 0), green)
}

sequence = []         # Последовательность, которую игрок формирует
player_sequence = []  # Последовательность, которую игрок повторяет
input_phase = 'record'  # 'record' - игрок выбирает следующий шаг, 'repeat' - повторяет всю последовательность
game_over = False

def draw_squares(highlight=None):
    for num, (color, rect) in colors.items():
        c = color
        if highlight == num:
            c = (255, 255, 255)  # подсветка белым при клике
        pg.draw.rect(screen, c, rect)

def show_message(text):
    img = font.render(text, True, (255, 255, 255))
    rect = img.get_rect(center=(screen.get_width() // 2, 450))
    screen.blit(img, rect)

def reset_game():
    global sequence, player_sequence, input_phase, game_over
    sequence = []
    player_sequence = []
    input_phase = 'record'
    game_over = False

reset_game()

while True:
    screen.fill((0, 0, 0))
    mpos = pg.mouse.get_pos()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN and not game_over:
            clicked_num = None
            for num, (_, rect) in colors.items():
                if rect.collidepoint(mpos):
                    clicked_num = num
                    break

            if clicked_num is not None:
                if input_phase == 'record':
                    # Игрок добавляет новый шаг в последовательность
                    sequence.append(clicked_num)
                    player_sequence = []
                    input_phase = 'repeat'
                elif input_phase == 'repeat':
                    # Игрок повторяет последовательность
                    player_sequence.append(clicked_num)
                    # Проверяем правильность на текущем шаге
                    if player_sequence[-1] != sequence[len(player_sequence) - 1]:
                        game_over = True
                    elif len(player_sequence) == len(sequence):
                        # Успешно повторил всю последовательность - переходим к записи следующего шага
                        player_sequence = []
                        input_phase = 'record'

        if event.type == pg.KEYDOWN and game_over:
            if event.key == pg.K_r:
                reset_game()

        if len(sequence) == 10:
            exit()

    # Рисуем квадраты
    draw_squares()

    # Выводим подсказки
    if game_over:
        show_message("Вы проиграли! Нажмите R для рестарта")
    else:
        if input_phase == 'record':
            show_message("Выберите следующий квадрат для запоминания")
        else:
            show_message(f"Повторите последовательность из {len(sequence)} шагов")

    pg.display.update()
    clock.tick(60)