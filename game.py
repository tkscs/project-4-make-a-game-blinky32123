import pygame  
import random
import sys  # <--- Add this line

Blue=(0,0,225)
Red =(225,0,0)
Green =(0,225,0)
Black =(0,0,0)
White = (225,225,225)

list = [Blue, Red, Green, Black, White]

pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()

# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(White)
pygame.display.set_caption("Game")


#screen= pygame.display.set_mode((640,640))
#screen.fill(Blue)

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        #self.image = pygame.image.load("spiderparts.png")
        original_image = pygame.image.load("one_eye_monster.png")
        self.image = pygame.transform.scale(original_image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) 
 
      def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 


class Player(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        #self.image = pygame.image.load("templar.png").convert()
        original_image = pygame.image.load("templar.png")
        self.image = pygame.transform.scale(original_image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

      def update(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[pygame.K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[pygame.K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 


P1 = Player()
E1 = Enemy()
              
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    P1.update()
    E1.move()
    
    DISPLAYSURF.fill(White)
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
         
    pygame.display.update()
    FramePerSec.tick(FPS)        















# import pygame
# from pygame.locals import *
# pygame.init()
# FPS = pygame.time.Clock()
# FPS.tick(60)
# while True: #code that updates the game  while it runs 
#     # 
#     # 
#     # 
#     pygame.display.update()
# display_screen = pygame.display.set_mode((300,300)) #DISPLAYSURF?


# color1 = pygame.Color(0, 0, 0)         # Black
# color2 = pygame.Color(255, 255, 255)   # White
# color3 = pygame.Color(128, 128, 128)   # Grey
# color4 = pygame.Color(255, 0, 0)       # Red








# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()

