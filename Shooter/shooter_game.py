import pygame
import random
import time
import asyncio

'''
Final touches:
aliens(go from up to down and shoot you)

buff6
2 more rockets near you that shot when you shot
'''


pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0, 0, 255)

Bullets = pygame.sprite.Group()

BULLET_AMOUNT = 100

shoting_cooldown = (10)
shoting_cooldown_divieded_for = 0
LIFE = 3

enemy_MAX = 5
enemy_MIN = 1

time_for_bonus = 0
score = 0
lost = 0

time_for_bullets = 0

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.y = player_y
        self.rect.x = player_x

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Bullet(GameSprite):
    def update(self):
        if self.rect.y > 0:
            self.rect.y -= 20
            self.reset()
        else:
            self.kill()
        self.reset()

'''class EnemyBullet(GameSprite):
    def update(self):
        if self.rect.y < 0:
            self.rect.y += self.speed
            self.reset()
        else:
            self.kill()
        self.reset()'''

class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x < window_width - 80:
            self.rect.x += self.speed
        
    def fire(self):
        bullet = Bullet("bullet.png",(self.rect.x), (self.rect.y + self.rect.height//2 - 90),0)
        Bullets.add(bullet)
        print("Fired bullet")
        
#rocket
rocket = Player("rocket.png", 300, 430, 5)

class Enemy(GameSprite):
    def update(self):
        if self.rect.y < window_height:
            self.rect.y += self.speed
            self.reset()
        else:
            self.kill()

class megaEnemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_health, _Sprite__g = ''):
        pygame.sprite.Sprite.__init__(self)
        self.health = player_health
        self.image = pygame.transform.scale(pygame.image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.y = player_y
        self.rect.x = player_x
    def update(self, health):
        if health > 0:
            if self.rect.y < window_height:
                self.rect.y += self.speed
                self.reset()
            else:
                self.kill()
        else:
            self.kill()


class Bonus(GameSprite):
    def update(self):
        if self.rect.y < window_height:
            self.rect.y += 1
            self.reset()
        else:
            self.kill()

class bulletDrop(GameSprite):
    def update(self):
        if self.rect.y < window_height:
            self.rect.y += 1
            self.reset()
        else:
            self.kill()

'''class Elian(GameSprite):
    def fire_bullet():
        bullet = EnemyBullet("bullet.png",(self.rect.x), (self.rect.y),1)
        EnemyBullets.add(bullet)
        print("Enemy fired bullet")
    def update(self):
        amm = 0
        if self.rect.y < window_height:
            self.rect.y += self.speed
            amm += 1
            if amm > 1:
                bullet = Bullet("bullet.png",self.rect.x, self.rect.y,10)
                Bullets.add(bullet)
                print("Fired bullet")
                amm = 0
            self.reset()
        else:
            self.kill()'''

class Player_helper_right(GameSprite):
    def update(self):
        self.x = rocket.rect.x + 20
        self.reset()
        
class Player_helper_left(GameSprite):
    def update(self):
        self.x = rocket.rect.x - 20
        self.reset()

monsters = pygame.sprite.Group()
mega_monsters = pygame.sprite.Group()
bonuses = pygame.sprite.Group()
drop_bullets_group = pygame.sprite.Group()
'''EnemyBullets = pygame.sprite.Group()'''
Elians = pygame.sprite.Group()

#Game scene:
window_width = 700
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Shoter")
background = pygame.transform.scale(pygame.image.load('background.png'), (window_width, window_height))

#Game settings
Game = True
finish = False
clock = pygame.time.Clock()
FPS = 60

#font:
pygame.font.init()


gg = pygame.font.Font("freesansbold.ttf", 53)
lose = gg.render('YOU LOST!', True, (180, 0, 0))
win = gg.render('YOU WON!', True, (255, 215, 0))
font = pygame.font.Font("freesansbold.ttf", 35)

drop_of_bullets = bulletDrop('bulletdrop.png', random.randint(0, window_width - 45), 10, 3)
drop_bullets_group.add(drop_of_bullets)

text_hearts = font.render('Hearts: ' + str(LIFE), True, red)
textRect_hearts = text_hearts.get_rect()
textRect_hearts.center = (100, 50)

text_score = font.render('Score: ' + str(score), True, green)
textRect_score = text_score.get_rect()
textRect_score.center = (90, 100)

text_time = font.render('Time: ' + str(0), True, blue)
textRect_time = text_time.get_rect()
textRect_time.center = (80, 150)

time_start_of_game = time.time()


text_bullets = font.render('Bullets left: ' + str(BULLET_AMOUNT), True, white)
textRect_bullets = text_bullets.get_rect()
textRect_bullets.center = (155, 200)


game = True
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
   
    if finish != True:
        window.blit(background,(0,0))
        
        rocket.update()
        rocket.reset()
        
        monsters.update()
        bonuses.update()
        Bullets.update()
        mega_monsters.update(10)
        drop_bullets_group.update()
        Elians.update()
        #EnemyBullets.update()

        window.blit(text_hearts, textRect_hearts)
        text_hearts = font.render('Hearts: ' + str(LIFE), True, red)
        window.blit(text_score, textRect_score)
        text_score = font.render('Score: ' + str(score), True, green)
        window.blit(text_time, textRect_time)
        text_time = font.render('Time: ' + str(int(round(time.time() - time_start_of_game))), True, blue)
        window.blit(text_bullets, textRect_bullets)
        text_bullets = font.render('Bullets left: ' + str(BULLET_AMOUNT), True, white)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT] and BULLET_AMOUNT > 0:
            pygame.time.delay(100)
            rocket.fire()
            BULLET_AMOUNT-=1

        if len(monsters) <= 4:
            monster = Enemy("asteroid.png", random.randint(0, window_width - 45), 10, random.randint(enemy_MIN, enemy_MAX))
            monsters.add(monster)

        if len(mega_monsters) <= 0 and random.randint(1, 300) == 300:
            mega_monster = megaEnemy("mega-asteroid.png", random.randint(0, window_width - 45), 10, random.randint(enemy_MIN + 2, enemy_MAX + 2), 4)
            mega_monsters.add(mega_monster)
        
        '''if len(Elians) <= 0:
            eme = Elian("ufo.png", random.randint(0, window_width - 45), 10, random.randint(enemy_MIN + 1, enemy_MAX + 1))
            Elians.add(eme)'''

        if time_for_bullets > 1000:
            drop_of_bullets = bulletDrop('bulletdrop.png', random.randint(0, window_width - 45), 10, 3)
            drop_bullets_group.add(drop_of_bullets)
            time_for_bullets = 0
        else:
            time_for_bullets+=1

        if time_for_bonus > 1000:
            bouns_drop = Bonus("bonus.png", random.randint(0, window_width - 45), 10, random.randint(2, 5))
            bonuses.add(bouns_drop)
            time_for_bonus = 0
        else:
            time_for_bonus+=1

        for m in monsters:
            if pygame.sprite.collide_rect(rocket, m):
                LIFE -= 1
                m.kill()
        for ma in mega_monsters:
            if pygame.sprite.collide_rect(rocket, ma):
                LIFE -= 1
                ma.kill()
            
        for B in Bullets:
            for m in monsters:
                if pygame.sprite.collide_rect(B, m):
                    score += 1
                    m.kill()
                    B.kill()
            for ma in mega_monsters:
                if pygame.sprite.collide_rect(B, ma):
                    ma.health -= 1
                    B.kill()
                    if ma.health <= 0:
                        score += 5
                        ma.kill()
        
        for bd in drop_bullets_group:
            if pygame.sprite.collide_rect(rocket, bd):
                BULLET_AMOUNT += 50
                bd.kill()
                    
        for b in bonuses:
            if pygame.sprite.collide_rect(b, rocket):
                #buff
                a = random.randint(1,5)
                if a == 1:
                    #buff1
                    if rocket.speed <= 8:
                        rocket.speed += 1
                        print("Buff gave: rocket speed + 1")
                        #else
                        #goto 241
                if a == 2:
                    #buff2
                    if enemy_MAX > 2:
                        enemy_MAX -= 1
                        print("Buff gave: enemy speed lowered by 1")
                        #else
                        #goto 241
                if a == 3:
                    #buff3
                    LIFE += 1
                    print("Buff gave: 1 more heart")
                if a == 4:
                    #buff4
                    for m in monsters:
                        m.kill()
                    print("Buff gave: all asteroids cleared")
                if a == 5:
                    #buff5
                    score += 20
                    print("Buff gave: score + 20")

                b.kill()

        if LIFE <= 0:
            finish = True

        game_finished = True


    if finish:

        if game_finished: #runs only one time
            finished_game_time = round(time.time())
            game_finished = False
        
        window.blit(background,(0,0))


        text_hearts = font.render('Hearts: ' + str(0), True, red)
        window.blit(text_hearts, textRect_hearts)

        text_score = font.render('Score: ' + str(score), True, green)
        window.blit(text_score, textRect_score)

        text_time = font.render('Time: ' + str(round(finished_game_time - time_start_of_game)), True, blue)
        window.blit(text_time, textRect_time)


        time_lasted = gg.render('You Lasted for ' + str(round(finished_game_time - time_start_of_game)) + ' secends', True, (180, 0, 0))
        window.blit(time_lasted,(0,300))
        lose = gg.render('You lost!', True, (180, 0, 0))
        window.blit(lose,(220, 200))

    pygame.display.update()
    clock.tick(FPS)