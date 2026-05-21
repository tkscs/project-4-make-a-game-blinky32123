import pygame  
import random
import sys 

Blue=(0,0,225)
Red =(225,0,0)
Green =(0,225,0)
Black =(0,0,0)
White = (225,225,225)
transparent=(0,0,0,0)

list = [Blue, Red, Green, Black, White]

pygame.init()
FPS = 45
FramePerSec = pygame.time.Clock()

#screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Game")
font = pygame.font.SysFont('Arial', 50)


red_timer = 60
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
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
      
red_counting = False

class Player(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
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
x=0 
clock=pygame.time.Clock()     
counter=30
text=str(counter)
last_hit_time=0
iframe_duration=500

TIMER_EVENT=pygame.USEREVENT+1
pygame.time.set_timer(TIMER_EVENT, 1000)
while True:
    for event in pygame.event.get():
      if red_counting == False:
        DISPLAYSURF.fill(White)
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        pygame.display.update()
    P1.update()
    E1.move()
    current_time=pygame.time.get_ticks()
    pygame.display.update()
    enemy_rect=E1.rect
    player_rect=P1.rect
    if player_rect.colliderect(enemy_rect): 
      E1.rect.top=0
      E1.rect.center = (random.randint(30, SCREEN_WIDTH), SCREEN_HEIGHT)
      if current_time - last_hit_time > iframe_duration: 
        x=x+1
        print(x)
        last_hit_time=current_time
      
    if x>3 or red_timer < 60:
      DISPLAYSURF.fill(Red)
      red_counting = True
      red_timer = red_timer - 1
    if counter>0:
      counter-=1/FPS #must be 60?   
      text=str(counter// 1)
    if counter <0:
      pygame.time.set_timer(TIMER_EVENT,0)
      DISPLAYSURF.fill(Red)
      red_counting =True
    else:
      if red_counting == False:
        DISPLAYSURF.fill(White)
        P1.draw(DISPLAYSURF)
        E1.draw(DISPLAYSURF)
    if red_timer == 0:
       red_counting = False


    timer_surface = font.render(text, True, (Black))
    DISPLAYSURF.blit(timer_surface, (200, 0))
    pygame.display.update()
    FramePerSec.tick(FPS)        