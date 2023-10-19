from pygame import *
import random
font.init()




class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, w, h, speed):
        super().__init__()
        print(player_image)
        self.image = transform.scale(image.load(player_image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed
    
    
        
    def show_sprite(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Ball(GameSprite):
    def __init__(self,player_image, player_x, player_y, w, h, speed, speed_x, speed_y):
        super().__init__(player_image, player_x, player_y, w, h, speed)
        self.speed_x = speed_x
        self.speed_y = speed_y
    def update(self):
        self.rect.x+=self.speed_x
        self.rect.y+=self.speed_y
        if self.rect.y < 2 or self.rect.y > 423:
            self.speed_y*=-1
        if sprite.collide_rect(self, platform_l) or sprite.collide_rect(self, platform_r):
            self.speed_x*=-1

class Player(GameSprite):    
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 2:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 398:
            self.rect.y += self.speed
    
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 2:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 398:
            self.rect.y += self.speed
        

window = display.set_mode((700, 500))
display.set_caption('Table Tennis')

FPS = 60
game = True
finish = False
bullets_amount = 0
clock = time.Clock()
background = transform.scale(image.load('table.png'), (700, 500))

platform_l = Player('platform.png', 3, 200, 20, 100, 3)
platform_r = Player('platform.png', 677, 200, 20, 100, 3) 
ball = Ball('ball.png', 308, 208, 75, 75, 0, 2, 2)
font1 = font.Font(None, 60)
text1 = font1.render('Player 1 has won!', 1, (50, 250, 50))
text2 = font1.render('Player 2 has won!', 1, (250, 50, 50))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish == False:
        window.blit(background, (0, 0))
        platform_l.update_l()
        platform_r.update_r()
        platform_l.show_sprite()
        platform_r.show_sprite()
        ball.show_sprite()
        ball.update()
        if ball.rect.x >= 700:
            window.blit(text1, (325, 75))
            finish = True
        if ball.rect.x < -75:
            window.blit(text2, (325, 75))
            finish = True

    display.update()
    clock.tick(FPS)