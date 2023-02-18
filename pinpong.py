from pygame import *


back = (200, 255, 255)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))


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

clock = time.Clock()
FPS = 60
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(back)
        roketka_1.update_r()
        roketka_1.reset()
        roketka_2.update_l()
        roketka_2.reset()

    display.update()
    clock.tick(FPS)
    
