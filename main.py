#Создай собственный Шутер!
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

class Player(GameSprite):    
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 445:
            self.rect.y += self.speed
    
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 445:
            self.rect.y += self.speed
        

window = display.set_mode((700, 500))
display.set_caption('Table Tennis')

FPS = 60
game = True
finish = False
bullets_amount = 0
clock = time.Clock()
background = transform.scale(image.load('table.png'), (700, 500))

platform_l = Player('Безымянный.png', 5, 225, 10, 50, 2)
platform_r = Player('Безымянный.png', 685, 225, 10, 50, 2) 
ball = GameSprite('ball.png', 325, 225, 50, 50, 2)


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

    display.update()
    clock.tick(FPS)