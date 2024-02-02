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
    def update(self): 
        keys_pressed = key.get_pressed() 
        if keys_pressed [K_s] and self.rect.x > 5 : 
            self.rect.x -= self.speed   

            keys_pressed = key.get_pressed() 
        if keys_pressed [K_w] and self.rect.x < win_width - 80 : 
            self.rect.x += self.speed 

    def update(self): 
        keys_pressed = key.get_pressed() 
        if keys_pressed [K_s] and self.rect.x > 5 : 
            self.rect.x -= self.speed   

            keys_pressed = key.get_pressed() 
        if keys_pressed [K_w] and self.rect.x < win_width - 80 : 
            self.rect.x += self.speed 
#ігрова сцена 
win_width = 700 
win_height = 500 
window = display.set_mode((win_width, win_height)) 
display.set_caption("Shooter Game") 
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height)) 
#шрифти ы написи 
font.init() 
font2 = font.Font(None, 36) 
font1 = font.Font(None,80)
text_lose = font1.render("YOU LOSE" ,True ,(255, 0, 0))
text_win = font1.render("YOU WIN" ,True ,(0, 255, 0))
#зображення 
shliapa = 'шляпа.png' 
nagets = 'тфпуеі.png' 
texac = 'техас.avif'