from pygame import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import Qt
import random
font.init()

amount_1 = 0
amount_2 = 0


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

platform_l = Player('platform.png', 3, 200, 20, 100, 3.5)
platform_r = Player('platform.png', 677, 200, 20, 100, 3.5) 
ball = Ball('ball.png', 308, 208, 75, 75, 0, 4, 4)
return_button = GameSprite('Return_button.png', 270, 255, 80, 50, 0)
rating_button = GameSprite('Leaders_button.png', 350, 255, 80, 50, 0)
font1 = font.Font(None, 60)
text1 = font1.render('Player 1 has won!', 1, (50, 250, 50))
text2 = font1.render('Player 2 has won!', 1, (250, 50, 50))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x,y = e.pos
            if return_button.rect.collidepoint(x, y):
                finish == False
                ball.rect.x = 308
                ball.rect.y = 208
                amount_1=0
                amount_2=0
                
    
    text_score = font1.render(str(amount_1) + ' : ' + str(amount_2), 1, (50,50,250))
    if finish == False:
        window.blit(background, (0, 0))
        platform_l.update_l()
        platform_r.update_r()
        platform_l.show_sprite()
        platform_r.show_sprite()
        ball.show_sprite()
        ball.update()
        window.blit(text_score, (305, 10))

        if amount_1 == 1:
            window.blit(text1, (190, 200))
            return_button.show_sprite()
            #rating_button.show_sprite()
            finish = True
        if amount_2 == 1:
            window.blit(text2, (190, 200))
            return_button.show_sprite()
            #rating_button.show_sprite()
            finish = True

        if ball.rect.x >= 650:
            amount_1 += 1
            ball.rect.x = 308
            ball.rect.y = 208
            
        if ball.rect.x < -25:
            amount_2+=1
            ball.rect.x = 308
            ball.rect.y = 208
            
        
    display.update()
    clock.tick(FPS)