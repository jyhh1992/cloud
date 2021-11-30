import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Green Knight')

moving_left = False
moving_right = False
clock = pygame.time.Clock()
FPS = 120
BG = (144,201,120)
RED = (255, 0 , 0)
GRAVITY= 0.75
shoot = False
shield= False
scatter_img = pygame.image.load('img/attack.png').convert_alpha()
shield_img = pygame.image.load('img/shield.png').convert_alpha()

def draw_bg():
    screen.fill(BG)
    pygame.draw.line(screen, RED, (0,300), (SCREEN_WIDTH, 300))

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        
        img = pygame.image.load('img/enemy.png')
        
        self.image = img 
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        
        self.health = 25
        self.update_time = pygame.time.get_ticks()
        self.animation_list = []
        for i in range(5):
            img = pygame.image.load('img/enemy.png')
            image = pygame.transform.scale(img, (int(img.get_width()), int(img.get_height())))
            self.animation_list.append(img)
    def draw(self):
        screen.blit(self.image,self.rect)
    def attack(self):
        
        attack_img = pygame.image.load('img/attack.png')
        attack_rect = attack_img.get_rect()
        x=500
        y=500
        attack_rect.center = (x, y)
        screen.blit(attack_img,attack_rect)
    def update(self): #update cooldown
        #self.update_animation()
        self.check_alive()
        

    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        if pygame.time.get_ticks() - self.update_time >ANIMATION_COOLDOWN:
            self.update_time = pygame.time_get_ticks()
            self.frame_index +=1
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0 
    def check_alive(self):
        if self.health <= 0 :
            self.health = 0 
            self.speed = 0 
            self.alive = False
            death_img =pygame.image.load(f'img/e_death.png') 
            self.image = death_img

class Character(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, ammo, ammo_shield):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.char_type = char_type
        

        self.health = 100
        self.max_health = self.health

        self.shoot_cooldown = 0
        self.shield_cooldown = 0 
        
        self.ammo = ammo 
        self.start_ammo = ammo

        self.ammo_shield = ammo_shield
        self.start_ammo_shield = ammo_shield
        
        self.direction = 1
        self.vel_y = 0
        self.alive = True
        self.jump = False
        self.flip = False
        self.animation_list = []
        self.index = 0
        self.update_time = pygame.time.get_ticks()


        for i in range(5):
            img = pygame.image.load(f'img/{char_type}.png')
            image = pygame.transform.scale(img, (int(img.get_width()* scale), int(img.get_height()* scale)))
            self.animation_list.append(img)
        self.image = self.animation_list[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
    
    def shoot(self):
        if self.shoot_cooldown == 0 and self.ammo > 0 :
            self.shoot_cooldown= 5
            scatter = Scatter(self.rect.centerx + (self.rect.size[0] * self.direction), self.rect.centery, self.direction)
            scatter_group.add(scatter)
            self.ammo -= 1

    def shield(self):
        if self.shield_cooldown == 0 and self.ammo_shield > 0:
            self.shield_cooldown = 10
            shield = Shield(self.rect.centerx,self.rect.centery)
            shield_group.add(shield)
            self.ammo_shield -=1

    def update_animation(self):
        ANIMATION_COOLDOWN = 10
        if pygame.time.get_ticks() - self.update_time >ANIMATION_COOLDOWN:
            self.update_time = pygame.time_get_ticks()
            self.frame_index +=1
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0 
    
    def update(self): #update cooldown
        #self.update_animation()
        self.check_alive()
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        if self.shield_cooldown >0:
            self.shield_cooldown -= 1
    def check_alive(self):
        if self.health <= 0 :
            self.health = 0 
            self.speed = 0 
            self.alive = False  
            self.image = pygame.image.load(f'img/death.png')
    
    def move(self, moving_left, moving_right):
        dx = 0
        dy = 0

        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        if self.jump == True:
            self.vel_y = -11
            self.jump = False
        self.vel_y += GRAVITY
        dy += self.vel_y
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
        self.rect.x += dx
        self.rect.y += dy

class Scatter(pygame.sprite.Sprite):
    def __init__(self,x,y,direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = scatter_img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction
        self.update_time = pygame.time.get_ticks()
    def update(self):
        #move bullet
        self.rect.x += (self.direction * self.speed)
        #check if bullet has gone off screen
        if self.rect.right <0 or self.rect.left >SCREEN_WIDTH:
            self.kill()
        
        #check collision with characters
        if pygame.sprite.spritecollide(player, scatter_group, False):
            if player.alive:
               player.health -= 5
            self.kill()
        if pygame.sprite.spritecollide(boss, scatter_group, False):
            
            if boss.alive:
                boss.health -= 25
                self.kill()

class Shield(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = shield_img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
        self.update_time = pygame.time.get_ticks()
    def update(self):
        
        
        
        #check collision with characters
        if pygame.sprite.spritecollide(scatter_group, shield_group, False):
            self.kill()
                   
        

scatter_group = pygame.sprite.Group()
shield_group = pygame.sprite.Group()

player = Character('player',200, 200, 1, 5, 100,5)

#enemy1 = Character('enemy',400,200,0.05,5)
#enemy2 = Character('enemy',500,200,0.05,5)

boss = Obstacle(500,250)
run = True

while run:
    clock.tick(FPS)

    draw_bg()
    player.update()
    player.draw()
    #enemy1.draw()
    #enemy2.draw()
    boss.draw()
    boss.attack()
    boss.update()
    scatter_group.update()
    scatter_group.draw(screen)
    
    shield_group.update()
    shield_group.draw(screen)
    #update player action 
    
    if shoot:
        player.shoot()
    
    elif shield:
        player.shield()
        
    player.move(moving_left,moving_right)
    clock.tick(FPS)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
        if player.alive ==True :    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    moving_left = True
                if event.key == pygame.K_d:
                    moving_right = True
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    shoot = True
                if event.key == pygame.K_g:
                    shield = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    moving_left = False
                if event.key == pygame.K_d:
                    moving_right = False
                if event.key == pygame.K_w:
                    player.jump = True
                if event.key == pygame.K_SPACE:
                    shoot = False
        else:
            shoot = False
    pygame.display.update()


pygame.quit()
