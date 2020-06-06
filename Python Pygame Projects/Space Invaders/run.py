import pygame 
import time
import random
import math
from pygame import mixer

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Lovi's Space Invaders")
pygame.display.set_icon(pygame.image.load('icon.png'))

Enemies = [pygame.image.load('Enemies/colores.png'),pygame.image.load('Enemies/enem.png'),pygame.image.load('Enemies/enemy2.png')]
Player_img = pygame.image.load('Player\\player1.png')
background = [pygame.image.load('Background\\bg1.jpg'),]
bullet_imgs = [pygame.image.load('Bullets\\flower1.png'),pygame.image.load('Bullets\\lasery.png'),pygame.image.load('Bullets\\bullet1.png')]
explosion = [pygame.image.load('Explosion\\explosion1.png'),pygame.image.load('Explosion\\explosion2.png')]
Enemy_bullets = [pygame.image.load('Enemies\\EBullet\\virus1.png'),pygame.image.load('Enemies\\EBullet\\virus2.png'),pygame.image.load('Enemies\\EBullet\\virus3.png')]

Enemies_array = []
bullets_array = []
enemy_bullet_array = []
enemy_positions = [i for i in range(4)]
num_of_enemies = 4
num_of_bullets = 5

FPS = 19

score_value = 0
font = pygame.font.Font('Font\\space age.ttf',48)
game_over = pygame.font.Font('Font\\hello honey.otf',104)
game_over1 = pygame.font.Font('Font\\hello honey.otf',84)
game_start = pygame.font.Font('Font\\Stars Fighters.ttf',16)
game_start1 = pygame.font.Font('Font\\Stars Fighters.ttf',13)

Game_lost = False
Start_game = True
run = True
Lives = 3 
Level = 0

# Sounds
mixer.music.load('Music\\bgm1.mp3')
mixer.music.queue('Music\\bgm2.mp3')
mixer.music.play(-1)

explosion_sound = mixer.Sound('Music\\Explosion.wav')
explosion_sound.set_volume(0.5)
bullet_sound = mixer.Sound('Music\\Laser.wav')
bullet_sound.set_volume(0.8)

score_textX = 0
score_textY = 0

collision = False
cooldown = 0

class Player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.change = 8
        self.jumpCount = 0
        self.isJump = False
        self.right = False
        self.left = False
    
    def draw(self,screen):
        screen.blit(Player_img,(self.x,self.y))


class Enemy(object):
    COOLDOWN = 35

    def __init__(self,x,y,height,width):
        self.x = x
        self.y = y
        self.num = -1
        self.height = 64
        self.width = 64
        self.left = False
        self.right = False
        self.facing = 0
        self.change_x = 18
        self.change_y = 40
        self.lasers = []
        self.cooldown = 0
    
    def draw(self,screen,num):
        screen.blit(Enemies[num%3],(self.x,self.y))
    
    def Cooldown(self):
        if self.cooldown >= self.COOLDOWN:
            self.cooldown = 0
        elif self.cooldown > 0:
            self.cooldown += 1

    def Shoot(self):
        if self.cooldown == 0:
            laser = Enemy_Bullet(self.x,self.y)
            enemy_bullet_array.append(laser)
            self.cooldown = 1
    

class Enemy_Bullet(Enemy):

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.attack_val = 15
    
            
    def draw(self,screen):
        screen.blit(Enemy_bullets[0],(self.x,self.y))

class Bullet(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.val = 15
    
    def draw(self,screen):
        screen.blit(bullet_imgs[0],(self.x,self.y))


def reDrawGameWindow():
    global collision
    screen.blit(background[0],(0,0))
    
    for bullet in bullets_array:
        bullet.draw(screen)
    
    for enemy in Enemies_array:
        enemy.draw(screen,Enemies_array.index(enemy))
        if collision:
            screen.blit(explosion[1],(enemy.x+(enemy.facing*8),enemy.y))
        collision = False
    
    for e_bullets in enemy_bullet_array:
        e_bullets.draw(screen)

    Player.draw(screen)
        
    score = font.render(f"Score: {str(score_value)}",True,(255,255,255))
    screen.blit(score,(score_textX,score_textY))

    lives = font.render(f"Lives : {str(Lives)}",True,(255,255,255))
    screen.blit(lives,(800-lives.get_width(),0))

    level = font.render(f"Level : {str(Level)}",True,(255,255,255))
    screen.blit(level,(800-level.get_width(),lives.get_height()+10))

    pygame.display.update()

def Start():
    global run
    global Start_game
    while Start_game:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Start_game = False
                run = False
                return None
        
            if event.type == pygame.KEYDOWN:
                Start_game = False
                return None

        GameStart1 = game_start.render(f"Welcome To Space Invaders Game",True,(0,255,0))
        screen.blit(GameStart1,(70 , round(screen.get_height()/2-92)))
        GameStart2 = game_start.render(f"By Lovish",True,(255,255,0))
        screen.blit(GameStart2,(300 , round(screen.get_height()/2-46) ))
        GameStart3 = game_start1.render(f"If You any suggestions Kindly Tell me",True,(0,255,0))
        screen.blit(GameStart3,(90 , 500))
        GameStart4 = game_start.render(f"Press Any Key To continue!",True,(0,255,255))
        screen.blit(GameStart4,(110 , round(screen.get_height()/2+6)))

        pygame.display.set_caption("Lovi's Space Invaders - Start Game")
        
        pygame.display.update()

def isColloide(ex,ey,bx,by):
    distance = math.sqrt((math.pow(ex-bx,2)) + (math.pow(ey-by,2)))
    if distance <= 30:
        return True
    return False

def enm_pl_colloide(ex,ey,px,py):
    distance = math.sqrt((math.pow(ex-px,2)) + (math.pow(ey-py,2)))
    if distance <=30:
        return True
    return False

def Lost_Game():
    global Game_lost
    global run
    while Game_lost:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game_lost = False
                run = False
                return None
        
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    run = False
                    return None
        
        Game_Quit = game_over.render(f"Game Over!",True,(255,0,0))
        screen.blit(Game_Quit,(round(screen.get_width()/2)-170,round(screen.get_height()/2)-52))
        score = game_over1.render(f"Score: {str(score_value)}",True,(255,255,255))
        screen.blit(score,(round(screen.get_width()/2)-170,round(screen.get_height()/2)-152))
        Thanks = game_over1.render(f"Thanks For Playing",True,(255,255,255))
        screen.blit(Thanks,(round(screen.get_width()/2)-220,round(screen.get_height()/2)+52))
        Lovi = game_over1.render(f"Lovi",True,(255,255,255))
        screen.blit(Lovi,(round(screen.get_width()/2)-Lovi.get_width()/2,round(screen.get_height()/2)+152))

        pygame.display.set_caption("Lovi's Space Invaders- You Lost")

        pygame.display.update()

Player = Player(400,500,64,64)

while run:
    clock.tick(FPS)
    
    if Start_game:
        Start()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if len(bullets_array) < num_of_bullets:
            bullets_array.append(Bullet(round(Player.x-Player.width//2-2),round(Player.y)))
            bullet_sound.play()

    if keys[pygame.K_LEFT] and Player.x>Player.change:
        Player.x -= Player.change
        Player.left = True
        Player.right = False

    elif keys[pygame.K_RIGHT] and Player.x <= (800-Player.width-Player.change): 
        Player.x += Player.change
        Player.right = True
        Player.left = False

    for bullet in bullets_array:
        if bullet.y < screen.get_height() and bullet.y > 0:
            bullet.y -= bullet.val
        else:
            bullets_array.pop(bullets_array.index(bullet))
    
    for enemy in Enemies_array:
        enemy.Cooldown()
        enemy.Shoot()

        if score_value<6:
            e_change_x = 8
            Level = 0

        elif score_value >= 6 and score_value<15:
            e_change_x = 9
            Level = 1

        elif score_value >= 15 and score_value<25:
            e_change_x = 11
            num_of_enemies = 6
            num_of_bullets =6
            Level = 2

        elif score_value >= 25 and score_value<45:
            e_change_x = 13
            Level = 3

        elif score_value >= 45 and score_value<80:
            e_change_x = 16
            num_of_enemies = 8
            num_of_bullets = 7
            Level = 4

        elif score_value >= 80 and score_value<110:
            e_change_x = 20
            Level = 5

        elif score_value >= 110 and score_value<150:
            e_change_x = 25
            Level = 6

        elif score_value >= 150 and score_value<200:
            e_change_x = 35
            num_of_enemies = 11
            Level = 7

        elif score_value >= 200 and score_value<260:
            e_change_x = 50
            num_of_enemies = 15
            num_of_bullets = 9
            Level = 8

        elif score_value >= 260 and score_value<330:
            e_change_x = 70
            num_of_enemies = 13
            Level = 9

        elif score_value >= 330 and score_value<410:
            e_change_x = 90
            num_of_enemies = 20
            num_of_bullets += 2
            Level = 10

        else:
            e_change_x = 130
            num_of_enemies = 30
            Level = "Max"
        
        if enemy.x <= 0:
            enemy.change_x = +e_change_x
            enemy.y += enemy.change_y
            enemy.left = False
            enemy.right = True
            enemy.facing = 1

        elif enemy.x + enemy.width >= 800:
            enemy.change_x = -e_change_x
            enemy.y += enemy.change_y
            enemy.right = False
            enemy.left = True
            enemy.facing = -1

        enemy.x += enemy.change_x
        enemy.facing = 0

    if len(Enemies_array) < num_of_enemies:
        Enemies_array.append(Enemy(random.randint(0,736),random.randint(0,200),64,64))
        
    for e_bullets in enemy_bullet_array:
        if e_bullets.y >0 and e_bullets.y<screen.get_height():
            e_bullets.y += e_bullets.attack_val
        else:
            enemy_bullet_array.pop(enemy_bullet_array.index(e_bullets))

    for enemy in Enemies_array:
        enemy.Shoot()
        for bullet in bullets_array:
            if isColloide(enemy.x,enemy.y,bullet.x,bullet.y):
                collision = True
                score_value += 1
                explosion_sound.play()
                bullets_array.pop(bullets_array.index(bullet))
                Enemies_array.pop(Enemies_array.index(enemy))
                break

    for enemy in Enemies_array:
        if enm_pl_colloide(enemy.x,enemy.y,Player.x,Player.y) or enemy.y > 600-enemy.height:
            Lives -= 1
            Enemies_array.pop(Enemies_array.index(enemy))
            explosion_sound.play()
            if Lives <= 0:
                Game_lost = True
                Lost_Game()
            break
    
    for e_bullets in enemy_bullet_array:
        if enm_pl_colloide(e_bullets.x,e_bullets.y,Player.x+32,Player.y+32):
            Lives = Lives-1
            enemy_bullet_array.pop(enemy_bullet_array.index(e_bullets))
            explosion_sound.play()
            if Lives <= 0:
                Game_lost = True
                Lost_Game()
            break
    
    reDrawGameWindow()
    


'''
To-do:
1. Start Color Scheme
2. Health
3. explosion sound on collision of enemy with limit and Player
4. My Name to prove originality
5. Distance Formula during collision
'''