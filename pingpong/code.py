from pygame import *
from random import *
font.init()
window = display.set_mode((700,500))
display.set_caption('ping_pong')
background = transform.scale(image.load('phon.png'),(700,500))
game = True
finish = False
class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x, player_y,player_speed,a,b):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(a,b))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed2 = self.speed
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 390:
            self.rect.y += self.speed
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 390:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def update(self):
        self.rect.x -= self.speed2
        self.rect.y+=self.speed
        if self.rect.y == 460:
            self.speed = self.speed *(-1)
        if self.rect.y==0:
            self.speed = self.speed*(-1)    
        
rprav = Player2('rprav.png',0,250,2,20,110)
rlev = Player1('rlev.png',680,250,2,20,110)
sharik = Enemy('sharik.png',350,250,2,40,40)
while game == True:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    rprav.reset()
    rprav.update()
    rlev.reset()
    rlev.update()
    sharik.reset()
    sharik.update()
    display.update()
