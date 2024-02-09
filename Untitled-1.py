from pygame import *

class GameSprite(sprite.Sprite): 

    def __init__(self, player_image , player_x , player_y, size_x, syze_y, player_speed): 
        sprite.Sprite.__init__(self) 
        self.image = transform.scale(image.load(player_image),(50 , 50))  
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
    def reset (self): 
        window.blit(self.image,(self.rect.x , self.rect.y)) 

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
#ігрова сцена:
back = ("завантаження.png")  #колір фону (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
 
#прапорці, що відповідають за стан гри
game = True
finish = False
clock = time.Clock()
FPS = 30
 
#створення м'яча та ракетки 
texas1 = Player('тфпуеі.png', 30, 200, 4, 50, 150) 
texas2 = Player('тфпуеі.png', 520, 200, 4, 50, 150)
shliapa = GameSprite('шляпа.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
 
speed_x = 1
speed_y = 1

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 
    if finish != True:
        window.fill(back)
        texas1.update_l()
        texas2.update_r()
        shliapa.rect.x+=speed_x
        shliapa.rect.y+=speed_y

        if sprite.collide_rect(texas1, shliapa) or sprite.collide_rect(texas2, shliapa):
            speed_x*= -1
            speed_y*= 1


        if shliapa.rect.y > win_height-50 or shliapa.rect.y < 0:
            speed_y *= -1

        if shliapa.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

        if shliapa.rect.x > win_width:
            finish = True
            window.blit(lose2, (2, 200))
            game_over = True

        texas1.reset()
        texas2.reset()
        shliapa.reset()

    display.update()
    clock.tick(FPS)


