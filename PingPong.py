from pygame import *
win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))

display.set_caption('Пинг Понг')
background = transform.scale(image.load('stadion.jpg'), (win_width, win_height))

font.init()
font1 = font.SysFont("Arial", 36)

FPS = 60
game = True
finish = False
clock = time.Clock()

player1_win = font1.render('Игрок 1 победил! ', 1, (0, 255, 47))
player2_win = font1.render('Игрок 2 победил! ', 1, (255, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:

        window.blit(background, (0, 0))


    




    display.update()
    clock.tick(FPS)