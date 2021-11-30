import pygame
import sys
from time import clock_getres, sleep

pygame.init()

BLACK = (0,0,0)
Width= 640
Height= int(Width*0.8)

screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("pyshoot")


#define player action variables
moving_left = False
moving_right = False




class Solider(pygame.sprite.Sprite):
    def __init__(self,x,y,scale):
        pygame.sprite.Sprite.__init__(self)
        img =pygame.image.load('/home/ubuntu/shoot/img/player/Idle/0.png')
        self.image =  pygame.transform.scale(img, (int(img.get_width()*scale),int(img.get_height()*scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def draw(self):
        screen.blit(self.image, self.rect)


player = Solider(200,200,3)
player2 = Solider(400,400,3)





run = True
while run:

    player.draw()

    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run=False
        # keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_ESCAPE:
                run = False

        #keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
        

    pygame.display.update()
 
pygame.quit() 




# def initGame():
#     global gamePad, clock
#     pygame.init()
#     gamePad = pygame.display.set_mode((Width,Height))
#     pygame.display.set_caption("pyshooting")
#     clock = pygame.time.Clock()

# def runGame():
#     global gamePad, clock
#     onGame = False
#     while not onGame:
#         for event in pygame.event.get():
#             if event.type in [pygame.QUIT]:
#                 pygame.quit()
#                 sys.exit()
#         gamePad.fill(BLACK) #게임 화면 (검은색)

#         pygame.display.update() # 게임화면을 다시그림

#         clock.tick(60) # 게임화면 초당 프레임수를 60으로 설정
#     pygame.quit() # pygame 종료


# initGame()
# runGame()
