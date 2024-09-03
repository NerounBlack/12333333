from typing import Any
from pygame import *
wn = display.set_mode((1920-400,1080-300))
display.set_caption("")

clock = time.Clock()

background = transform.scale(image.load("png/fon.png"),(1920-400,1080-300))
background2 = transform.scale(image.load("png/fon2.png"),(1920-400,1080-300))
game = True
# mixer.init()
#mixer.music.load("jungles.ogg")
# mixer.music.play()
# kick = mixer.Sound("jungles.ogg")
# mony = mixer.Sound("money.ogg")



class Game_Sprite(sprite.Sprite):
    def __init__(self, imagepl, speed, player_x, player_y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load("png/"+imagepl), (size_x,size_y))
        self.speed=speed
        self.rect=self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        wn.blit(self.image,(self.rect.x,self.rect.y))

class Hero(Game_Sprite):
    def update(self):
        k =key.get_pressed()

        if k[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if k[K_d] and self.rect.x < 1920-400-60:
            self.rect.x += self.speed

        
    def grav(self):
        if self.rect.y < 450:
            self.rect.y+=self.speed



class Enemy(Game_Sprite):
    direction = "right"

    def update(self,x1,x2):
    
        if self.rect.x < x1 :
            self.direction = "right"
        if self.rect.x > x2:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed

        if self.direction == "right":
            self.rect.x += self.speed

        

class Area():
    def __init__(self, x=0, y=0, width =10, height =10, color=None):
        self.rect = Rect(x, y, width, height)#прямокутник
        self.fill_color = color


    def color(self, new_color):
        self.fill_color = new_color


    def draw(self):
        draw.rect(wn,self.fill_color,self.rect)

bx = 0
mario = Hero("mario.png", 10, 1220, 450, 225, 225)

gribocks = sprite.Group()
redmushroom = Enemy("redmushroom.png", 3, 300,590,90,90)
bluemushroom = Enemy("bluemushroom.png", 3, 700,578,100,100)
purplemushroom = Enemy("purplemushroom.png", 3, 1000, 585, 100,100)
gribocks.add(redmushroom)
brick1 = Enemy("brick.png", 3, 450,587,90,90)
brick2 = Enemy("brick.png", 3, 550,500,90,90)
brick3 = Enemy("brick.png", 3, 450,587,90,90)


gribocks.add(bluemushroom)
gribocks.add(purplemushroom)
tryba = Enemy("tryba.png", 3, 1200, 450,300,300 )

color = (134,132,124)
l1block = Area(1345, 515,10,10, color)

gtaf_e = True
level_1 = 0
hp = 3
heart_list= []
heart_x = 10
for i in range(3):
    heart = Game_Sprite("hurt.png", 3, heart_x,10,100,80)
    heart_list.append(heart)
    heart_x += 100

level_2 = 1

jumping = False
jump_count = 12
jump_height = 12
space_pressed = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        k =key.get_pressed()
        if k[K_1]:
            game = False
    if not jumping:
        if k[K_SPACE] and not space_pressed:
            jumping = True
            space_pressed = True  # Mark spacebar as pressed
    else:
        if jump_count >= -jump_height:
            neg = 1
            if jump_count < 0:
                neg = 0
            mario.rect.y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = jump_height
    if not k[K_SPACE]:
        space_pressed = False
    if level_1:
        l1block.draw()
        wn.blit(background,(bx,0))
        wn.blit(background,(bx-(1920-400),0))
        bx+=2
        if bx >= 1920-400:
            bx = 0
        if gtaf_e:
            mario.grav()
            
        bottom_rect = Rect(mario.rect.left, mario.rect.bottom, mario.rect.width, 1)
        if bottom_rect.colliderect(l1block.rect):
            gtaf_e = 0

        
            
        else:
            gtaf_e = 1

        if mario.rect.colliderect(redmushroom):
            if heart_list:
                
                heart_list.pop()
                mario.rect.x   -= 100

        if mario.rect.colliderect(bluemushroom):
            if heart_list:

                heart_list.pop()

        if mario.rect.colliderect(purplemushroom):
            if heart_list:

                heart_list.pop()
                mario.rect.x += 100


        mario.reset()
        mario.update()
        redmushroom.reset()
        redmushroom.update(300,400)
        bluemushroom.update(700,720)
        bluemushroom.reset()
        purplemushroom.reset()
        purplemushroom.update(1000,1050)
        tryba.reset()    
        for heart in heart_list:
            heart.reset()   

    if level_2:
        wn.blit (background2, (0,0))
        mario.reset()
        mario.update()
        mario.grav()
        brick1.reset()
        brick2.reset()
        brick3.reset()
    clock.tick(60)
    display.update()




