import pygame
from random import randint
import time
pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
ground = pygame.image.load("images\ground.png")
a_1 = pygame.image.load("frame_01_delay-0.05s-removebg-preview.png")
a_2 = pygame.image.load("frame_04_delay-0.05s-removebg-preview.png")
a_3 = pygame.image.load("frame_07_delay-0.05s-removebg-preview.png")
a_4 = pygame.image.load("frame_10_delay-0.05s-removebg-preview.png")
restart_img = pygame.image.load("images\Restart.png")
booster_img = pygame.image.load("images\Booster.png")
obstacle_img = pygame.image.load("images\Box_2.png")
font = pygame.font.SysFont("Calibri", 40, bold=True, italic=False)
obstacle_img = pygame.transform.scale(obstacle_img, (100,100))
booster_img = pygame.transform.scale(booster_img, (100,100))
a_1 = pygame.transform.scale(a_1, (332,250))
a_2 = pygame.transform.scale(a_2, (332,250))
a_3 = pygame.transform.scale(a_3, (332,250))
a_4 = pygame.transform.scale(a_4, (332,250))
ground_x = 0
score = 0
lives = 3
Lives_text = font.render(str(round (lives, 2)), True, (66, 38, 38))
obstacle_gap = 300
obstacle_frequency = 1800
images = [a_1, a_2, a_3, a_4]
walking = False
game = True
last_obstacle = pygame.time.get_ticks() - obstacle_frequency

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,x, y):
            super().__init__()
            self.x = x
            self.y = y
            self.image = obstacle_img
            self.rect = self.image.get_rect()
            self.rect.center = x, y
    def update(self):
        self.rect.x -= 3
        if self.rect.x < 0:
            self.kill()
class Booster(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = booster_img
        self.rect = self.image.get_rect()
        self.rect.center = x, y
    def update(self):
        self.rect.x -= 3
        if self.rect.x < 0:
            self.kill()

class Walk(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = images
        self.index = 0
        self.counter = 0
        self.image = self.images[self.index]
        self.x = x
        self.y = y
        self.clicked = False
        self.velocity = 0
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
    def update(self):
        if game == True:
            self.counter += 1
            if self.counter > 10:
                self.counter = 0
                self.index += 1
                print(self.index)
                if self.index >= 4:
                    self.index = 0
            self.image = self.images[self.index]
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.velocity = -3
            elif pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
Booster_group = pygame.sprite.Group()
Boy_group = pygame.sprite.Group()
Obstacle_group = pygame.sprite.Group()
Boy = Walk(100, 425)
Boy_group.add(Boy)

run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("sky blue")
    screen.blit(ground, (ground_x, 520))
    timenow = pygame.time.get_ticks()
    if timenow - last_obstacle > obstacle_frequency:
        h = randint(-100, 100)
        bottom_obstacle = Obstacle(800, 480)
        Obstacle_group.add(bottom_obstacle)
        last_obstacle = timenow
    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            Obstacle_group.empty()
            walking = False
            Boy.rect.x = 100
            Boy.rect.y = 300
            game = True
    if run == True:
        ground_x -= 0.2
        if abs(ground_x) > 35:
            ground_x = 0
    if game == True:
        Score_text = font.render("Score:"+str(round (score, 2)), True, (66, 38, 38))
        score += 0.02
        if pygame.sprite.groupcollide(Boy_group, Obstacle_group, False, True):
            lives -= 1
            Lives_text = font.render("Lives:"+str(round (lives, 2)), True, (66, 38, 38))
            if lives < 1:
                score = 0
                lives = 3
                Obstacle_group.update()
                game = False
                screen.blit(restart_img, (300, 300))
                pygame.display.update()
                time.sleep(1)
    Boy_group.update()
    Boy_group.draw(screen)
    Obstacle_group.draw(screen)
    screen.blit(Score_text, (50, 50))
    screen.blit(Lives_text, (150, 150))
    pygame.display.update()
