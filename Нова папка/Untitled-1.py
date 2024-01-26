from pygame import * 
from random import randint 
#звук 
mixer.init() 
mixer.music.load("space.ogg") 
mixer.music.play() 
fire = mixer.Sound("fire.ogg") 
 
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
        if keys_pressed [K_LEFT] and self.rect.x > 5 : 
            self.rect.x -= self.speed   
 
            keys_pressed = key.get_pressed() 
        if keys_pressed [K_RIGHT] and self.rect.x < win_width - 80 : 
            self.rect.x += self.speed 
 
 
    def fire(self): 
        pass
        bullet = Bullet(bullet_img, self.rect.x, self.rect.y, 15, 20, -15)
        bullets.add(bullet)
bullets = sprite.Group()
#лічильник збитих і пропущених кораблів змінив на -20 з -15
     
score = 0 
lost = 0 
class Enemy(GameSprite): 
    def update(self): 
        self.rect.y += self.speed 
        global lost  
 
        if self.rect.y > win_height: 
            self.rect.x = randint(80, win_width - 80) 
            self.rect.y = 0 
            lost = lost + 1 
 
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
asteroid = 'asteroid.png' 
bullet_img = 'bullet.png' 
rocket = 'rocket.png' 
ufo = 'ufo.png' 
 
#спайти 
rocket = Player(rocket, 5, win_height - 100, 80, 100, 20) 
monsters = sprite.Group() 
for i in range(1, 6): 
    monster = Enemy(ufo, randint(80, win_width - 80), -40, 80, 50, randint(1, 5)) 
    monsters.add(monster)  




class Bullet (GameSprite):
    def update(self):
        self.rect.y += self.speed 
        #znukae aikscho diyde  do kraay ekrana
        if self.rect.y < 0:
            self.kill()
            

#змінна гра закінчилась 
 
finish = False 
 
 
#Основний цикл гри 
run = True 
 
while run: 
 
    #подія натискання на кнопку закрити 
     
    for e in event.get(): 
        if e.type == QUIT: 
            run = False 

        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire.play()
                rocket.fire()




    if not finish: 
 
        window.blit(background, (0, 0)) 
         
        #пишемо текст на екрані 
 
        text = font2.render("Рахунок:" + str(score), 1, (255, 255, 255)) 
        window.blit(text, (10, 20)) 
 
        text_raxynok = font2.render("Пропущено:" + str(lost), 1, (255, 255, 255)) 
        window.blit(text_raxynok, (10, 50)) 
 
        #рухи спрайтів 
 
        rocket.update() 
        monsters.update() 
        bullets.update()

        rocket.reset() 
        monsters.draw(window) 
        bullets.draw(window)
        if sprite.spritecollide(rocket, monsters, False):
            finish = True
            window.blit(text_lose, (200, 200))

        collides = sprite.groupcollide(monsters, bullets, True , True)
        for c in collides :
            monster = Enemy(ufo, randint(80, win_width - 80), -40, 80, 50, randint(1, 5)) 
            monsters.add(monster)  
            score += 1
        if score == 11:
            finish = True
            window.blit(text_win, (200, 200))
        if lost >= 11:
            finish = True
            window.blit(text_lose, (200, 200))
    
    else:
        score = 0
        lost = 0
        finish = False
        for m in monsters:
            m.kill()
        for b in bullets:
            b.kill()   

        time.delay(3000)
        for i in range(1, 6): 
            monster = Enemy(ufo, randint(80, win_width - 80), -40, 80, 50, randint(1, 5)) 
            monsters.add(monster)  
    display.update() 
 
    time.delay(50)