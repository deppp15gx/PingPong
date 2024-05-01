from pygame import *
from time import sleep
win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_press = key.get_pressed()
        if keys_press[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_press[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys_press = key.get_pressed()
        if keys_press[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_press[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

display.set_caption('Пинг Понг')
background = transform.scale(image.load('stadion.jpg'), (win_width, win_height))

font.init()
font1 = font.SysFont("Arial", 36)

player1 = Player('rocket2.png', 25, 200, 5, 80, 100)
player2 = Player('rocket1.png', 600, 200, 5, 80, 100)

ball = GameSprite('ball.png', 312, 200, 7, 80, 100)

FPS = 60
game = True
finish = False
clock = time.Clock()

player1_win = font1.render('Игрок 1 победил! ', 1, (0, 255, 47))
player2_win = font1.render('Игрок 2 победил! ', 1, (255, 0, 0))

speed_x = 3
speed_y = 3



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
  
        window.blit(background, (0, 0))

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
        player1.update_l()
        if ball.rect.x < 0:
            window.blit(player2_win, (200, 200))
            finish = True
        if ball.rect.x > win_width:
            window.blit(player1_win, (200, 200))
            finish = True
        player1.reset()
    
        player2.update_r()

        player2.reset()

        ball.reset()

    display.update()

    if finish == True:
        time.delay(3000)
        finish = False
        ball.rect.x = 312
        ball.rect.y = 200


    clock.tick(FPS)
