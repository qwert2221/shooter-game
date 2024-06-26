from pygame import *
from random import *
init()
 
counter_missings = 0
finish = False
score = 0
side = "right"
boss_a = True
n = 0
n2 = 0
n3 = 0
count_ufo = 0
move_bullet = False
move_left = False
move_right = True
move_left2 = True
move_right2 = False




RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

clock = time.Clock()
pygame_icon = image.load("icon-game.png")
 
window = display.set_mode((700,500))
display.set_caption('Shooter')
display.set_icon(pygame_icon)
 
 
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()


fire = mixer.Sound("fire.ogg")


font = font.SysFont("Arial", 50)


lose = font.render(
    "Ты проиграл!", True, RED
)

new_game = font.render(
    "Нажми esc чтобы начать игру заново", True, WHITE
)

missed_txt_game = font.render(
    "Пропущено:", True, WHITE
)

score_txt_game = font.render(
    "Счет:", True, WHITE
)

 
 
class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, speed = 5, w = 65, h = 65):
        super().__init__()
        self.w = w
        self.h = h
        self.image = transform.scale(image.load(img), (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
 
    def paint(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
 
class Rocket(GameSprite):
    def move(self):
        if keys[K_a] and self.rect.left >= 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.right <= 700:
            self.rect.x += self.speed
 
class Ufo(GameSprite):
    def update(self):
        global counter_missings
        global boss_a
        global n2
        global count_ufo
        self.rect.y += self.speed
        if self.rect.y >= 500 and boss_a == False:
            counter_missings += 1
            self.rect.y = -50
            self.rect.x = randint(10, 630)



class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()

class Meteor(GameSprite):
    def update(self):
        global score
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.rect.y = -50
            self.rect.x = randint(10, 630)
    
class Live(GameSprite):
    def update(self):
        global counter_missings
        

class Boss(GameSprite):
    def move_boss(self):
        global side
        if side == "right" and self.rect.x <= 330:
            self.rect.x += 1.5
        else:
            side = "left"

        if side == "left" and self.rect.x >= 30:
            self.rect.x -= 1
        else:
            side = "right"

class Bullet_Boss(GameSprite):
    def update(self):
        self.rect.y += self.speed

class Laser(GameSprite):
    def move_laser(self):
        global move_left
        global move_right
        global n2

        if move_right:
            self.rect.x += self.speed
            if self.rect.x >= randint(160, 300):
                move_right = False
                move_left = True
        if move_left:
            self.rect.x -= self.speed
            if self.rect.x <= -30:
                move_right = True
                move_left = False
                n2 = 0

    def move_laser_right(self):
        global move_left2
        global move_right2
        global n3

        if move_left2:
            self.rect.x -= self.speed
            if self.rect.x <= randint(350, 460):
                move_right2 = True
                move_left2 = False

        if move_right2:
            self.rect.x += self.speed
            if self.rect.x >= 740:
                move_right2 = False
                move_left2 = True
                n3 = 0

        
        

background = transform.scale(image.load('galaxy.jpg'), (700,500))
rocket = Rocket('rocket.png', 300, 430, 10)
boss = Boss("boss.png", 700//2-350//2, -40, 1.5, 350, 300)
asteroid1 = Meteor("asteroid.png", randint(10, 630), 0, 4, 80, 80)
asteroid2 = Meteor("asteroid.png", randint(10, 630), 0, 4, 80, 80)
ufo1 = Ufo('ufo.png', randint(10, 630), 0, 3)
ufo2 = Ufo('ufo.png', randint(10, 630), 0, 3)
ufo3 = Ufo('ufo.png', randint(10, 630), 0, 3)
ufo4 = Ufo('ufo.png', randint(10, 630), 0, 3)
ufo5 = Ufo('ufo.png', randint(10, 630), 0, 3)
live1 = Live("live.png", 620, 10, 0, 80, 40)
live2 = Live("live.png", 580, 10, 0, 80, 40)
live3 = Live("live.png", 540, 10, 0, 80, 40)
bullet_boss = Bullet_Boss("bullet boss.png", boss.rect.centerx + 10, boss.rect.y + 170, 10, 90, 110)
bullet_boss2 = Bullet_Boss("bullet boss.png", boss.rect.centerx - 10, boss.rect.y + 170, 10, 90, 110)
bullet_boss3 = Bullet_Boss("bullet boss.png", boss.rect.centerx, boss.rect.y + 170, 10, 90, 110)
laser = Laser("laser.png", -40, -100, 3, 70, 800)
laser_right = Laser("laser.png", 740, -100, 3, 70, 800)

 
 
ufos = sprite.Group()
ufos.add(ufo1)
ufos.add(ufo2)
ufos.add(ufo3)
ufos.add(ufo4)
ufos.add(ufo5)
 

bullets = sprite.Group()


asteroids = sprite.Group()
asteroids.add(asteroid1)
asteroids.add(asteroid2)


game = True
while game:
    keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
        if keys[K_SPACE]:
            bullets.add(Bullet("bullet.png", rocket.rect.centerx - 7, rocket.rect.top, 25, 25, 25))
            fire.play()
 
    score_game = font.render(
        str(score), True, WHITE
    )

    missed_game = font.render(
        str(counter_missings), True, WHITE
    )

    if finish != True:
        #printing
        window.blit(background, (0,0))
        rocket.paint()
        if boss_a != True:
            ufos.draw(window)
        bullets.draw(window)
        
        window.blit(score_txt_game, (10, 10))
        window.blit(score_game, (110, 10))
        #moves
        rocket.move()
        if boss_a != True:
            ufos.update()
        bullets.update()
    else:
        window.fill(BLACK)
        window.blit(lose, (240, 500//2-100))
        window.blit(new_game, (25, 250))
        if keys[K_ESCAPE]:
            finish = False
            counter_missings = 0
            score = 0

    #meteor
    if score >= 10 and finish != True:
        asteroids.draw(window)
        asteroids.update()

    #heart
    if counter_missings != 1 and counter_missings != 2 and counter_missings != 3:
        live3.paint()
    if counter_missings != 2 and counter_missings != 3:
        live2.paint()
    if counter_missings != 3:
        live1.paint()
        
    #lose
    if counter_missings >= 999:
        finish = True
 
    #collisions
    if sprite.groupcollide(bullets, ufos, True, True):
        score += 1
    if sprite.spritecollide(rocket, ufos, True):
        counter_missings += 1
    if sprite.spritecollide(rocket, asteroids, True):
        counter_missings += 1

        
    if len(ufos) < 5 and boss_a != True:
        ufos.add(Ufo('ufo.png', randint(10, 630), 0, 3))    


    if score >= 20:
        boss_a = True
        
    if boss_a == True:
        boss.paint()  
        boss.move_boss()

        #cpunter bullet boss
        if n != 30:
            n += 1
            move_bullet = False
        if n == 30:
            bullet_boss.paint()
            bullet_boss.update()
            bullet_boss2.paint()
            bullet_boss2.update()
            if bullet_boss.rect.y >= 600 and bullet_boss2.rect.y >= 600:
                bullet_boss.rect.x = boss.rect.centerx + 10
                bullet_boss.rect.y = boss.rect.y + 170
                bullet_boss2.rect.x = boss.rect.centerx - 10
                bullet_boss2.rect.y = boss.rect.y + 170
                n = 0
    #counter lasers
        if n2 != 160:
            n2 += 1
        if n2 == 160:
            laser.paint()
            laser.move_laser()

        if n3 != 200:
            n3 += 1
        if n3 == 200:
            laser_right.paint()
            laser_right.move_laser_right()



        
        
        


    
    



    
 
    display.update()
    clock.tick(60)
