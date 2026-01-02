import pygame
from random import randint
pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
sky = pygame.image.load("images\sky.png")
ground = pygame.image.load("images\ground.png")
pipe_img = pygame.image.load("images\pipe.png")
bird1 = pygame.image.load("images\Flap1.png")
bird2 = pygame.image.load("images\Flap2.png")
bird3 = pygame.image.load("images\Flap3.png")
images = [bird1, bird2, bird3]
ground_x = 0
game = True
run = True
flying = False
pipe_gap = 150
pipe_frequency = 2000
last_pipe = pygame.time.get_ticks() - pipe_frequency
class Pipe(pygame.sprite.Sprite):
    def __init__(self,x, y, pos):
            super().__init__()
            self.x = x
            self.y = y
            self.image = pipe_img
            self.rect = self.image.get_rect()
            if pos == 1:
                self.image = pygame.transform.flip(self.image, False, True)
                self.rect.bottomleft = x, y - pipe_gap / 2
            if pos == 0:
                self.rect.topleft = x, y + pipe_gap / 2
    def update(self):
        self.rect.x -= 2
        if self.rect.x < 0:
            self.kill()

class Bird(pygame.sprite.Sprite):
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
        if flying == True:
            self.velocity += 0.05
            if self.velocity > 4:
                self.velocity = 4
            if self.rect.bottom < 520:
                self.rect.y += self.velocity
        if game == True:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.velocity = -3.5
            elif pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            
            self.counter += 1
            if self.counter > 10:
                self.counter = 0
                self.index += 1
                if self.index >= 3:
                    self.index = 0
            self.image = self.images[self.index]
Bird_group = pygame.sprite.Group()
Pipe_group = pygame.sprite.Group()
clock = pygame.time.Clock()
Flappy = Bird(200, 250)
Bird_group.add(Flappy)
while run: 
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if flying == False and game == True:
                flying = True
    screen.blit(sky, (0, -120))
    screen.blit(ground, (ground_x, 520))
    Bird_group.draw(screen)
    Bird_group.update()
    Pipe_group.draw(screen)
    if Flappy.rect.bottom > 520:
        game = False
        flying = False
    if game == True:
        timenow = pygame.time.get_ticks()
        if timenow - last_pipe > pipe_frequency:
            h = randint(-100, 100)
            bottom_pipe = Pipe(800, HEIGHT / 2+ h, 0)
            top_pipe = Pipe(800, HEIGHT / 2 + h, 1)
            Pipe_group.add(bottom_pipe)
            Pipe_group.add(top_pipe)
            last_pipe = timenow
        ground_x -= 1
        if abs(ground_x) > 35:
            ground_x = 0
        Pipe_group.update()
    pygame.display.update()