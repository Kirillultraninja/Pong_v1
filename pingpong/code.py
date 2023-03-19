from pygame import *
from random import *
font.init()
s = font.SysFont('Arial',40)
window = display.set_mode((700,500))
display.set_caption('ping_pong')
background = transform.scale(image.load('phon.png'),(700,500))
game = True
finish = False
class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x, player_y,player_speed,a,b):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(a,b))
        self.y = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.x = player_speed
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.y
        if keys[K_DOWN] and self.rect.y < 390:
            self.rect.y += self.y
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.y
        if keys[K_s] and self.rect.y < 390:
            self.rect.y += self.y
class Enemy(GameSprite):
    def update(self):
        self.rect.x -= self.x
        self.rect.y+=self.y
counter = 10  
counter1 = 10      
rprav = Player1('rprav.png',680,250,2,20,110)
rlev = Player2('rlev.png',0,250,2,20,110)
sharik = Enemy('sharik.png',350,250,2,40,40)
while game == True:
    window.blit(background,(0,0))
    txt = 'Жизней:'+ str(counter)
    score = s.render(txt,True,(0,0,250))
    txt1 ='Жизней:'+ str(counter1)
    score1 = s.render(txt1,True,(0,0,250))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(score,(5,0))
        window.blit(score1,(530,0))
        rprav.reset()
        rprav.update()
        rlev.reset()
        rlev.update()
        sharik.reset()
        sharik.update()
        display.update()
        if sharik.rect.y == 460 or sharik.rect.y == 0:
            sharik.y *= -1
        if sharik.rect.x == -20:
            sharik.rect.x = 350
            sharik.rect.y = 250
            sharik.y *= -1
            sharik.x *= -1
            counter-=3
        if sharik.rect.x == 680: 
            sharik.rect.x = 350
            sharik.rect.y = 250
            sharik.y *= -1
            sharik.x *= -1
            counter1-=3
        if sprite.collide_rect(rlev,sharik):
            sharik.x *= -1
            counter+=1
        if sprite.collide_rect(rprav,sharik):
            sharik.x *= -1
            counter1+=1
        if counter <=0:
            finish = True
        if counter1 <=0:
            finish = True
    if finish ==True and counter <=0:
        txtfin1 ='Левый проиграл!'
        scorefin1 = s.render(txtfin1,True,(0,0,0))
        window.blit(scorefin1,(245,230))
        display.update()
    if finish ==True and counter1 <=0:
        txtfin2 ='Правый проиграл!'
        scorefin2 = s.render(txtfin2,True,(0,0,0))
        window.blit(scorefin2,(228,230))
        display.update()
