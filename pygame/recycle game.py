import pygame
from random import randint, choice
pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
green_earth = pygame.image.load("images\green_earth.png")
green_earth = pygame.transform.scale(green_earth, (800, 600))
Bin_img = pygame.image.load("images\Bin.png")
Bin_img = pygame.transform.scale(Bin_img, (80, 100))
plastic_bag = pygame.image.load("images\plastic_bag.png")
plastic_bag = pygame.transform.scale(plastic_bag, (40, 50))
paper_bag = pygame.image.load("images\paper_bag.png")
paper_bag = pygame.transform.scale(paper_bag, (40, 50))
pencil = pygame.image.load("images\pencil.png")
pencil = pygame.transform.scale(pencil, (40, 50))
box = pygame.image.load("images\Box.png")
box = pygame.transform.scale(box, (40, 50))
images = [paper_bag, box, pencil]
class Bin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = Bin_img
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
class Plastic(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = plastic_bag
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
class Recycle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = choice(images)
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
bin = Bin(350, 50)
Bin_group = pygame.sprite.Group()
Bin_group.add(bin)
Plastic_group = pygame.sprite.Group()
Recycle_group = pygame.sprite.Group()
for i in range(30):
    recycle = Recycle(randint(20, 780), randint(20, 580))
    Recycle_group.add(recycle)
for i in range(20):
    plastic = Plastic(randint(20, 780), randint(20, 580))
    Plastic_group.add(plastic)

run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            bin.rect.center = pos
    screen.fill("sky blue")
    screen.blit(green_earth, (0, 0))
    Bin_group.draw(screen)
    Plastic_group.draw(screen)
    Recycle_group.draw(screen)
    pygame.display.update()