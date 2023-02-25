from pygame import *
font.init()

back = (200, 255, 255)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
font1 = font.Font(None, 35)
lose1 = font1.render('ARTEM_1 LOSER!', True, (180, 0, 0))
lose2 = font1.render('ARTEM_2 LOSER!', True, (180, 0, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height -99:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height -99:
            self.rect.y += self.speed            
    
roketka_1 = Player('racket.png', win_width - 57, win_height -50, 10)
roketka_2 = Player('racket.png', win_width - 710, win_height -50, 10)
ball = GameSprite('tenis_ball.png', win_width - 700, win_height - 500, 5)
clock = time.Clock()
FPS = 60
finish = False
game = True

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y        
        window.fill(back)
        roketka_1.update_r()
        roketka_1.reset()
        roketka_2.update_l()
        roketka_2.reset()
        ball.reset()

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(roketka_1, ball) or sprite.collide_rect(roketka_2, ball):
            speed_x *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))    

        if ball.rect.x > win_width - 50:
            finish = True
            window.blit(lose2, (200, 200))  




    display.update()
    clock.tick(FPS)
