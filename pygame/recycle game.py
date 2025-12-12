import pygame
from random import randint, choice
import time
pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
green_earth = pygame.image.load("images\green_earth.png")
green_earth = pygame.transform.scale(green_earth, (800, 600))
Bin_img = pygame.image.load("images\Bin.png")
Bin_img = pygame.transform.scale(Bin_img, (60, 80))
plastic_bag = pygame.image.load("images\plastic_bag.png")
plastic_bag = pygame.transform.scale(plastic_bag, (40, 50))
paper_bag = pygame.image.load("images\paper_bag.png")
paper_bag = pygame.transform.scale(paper_bag, (40, 50))
pencil = pygame.image.load("images\pencil.png")
pencil = pygame.transform.scale(pencil, (40, 50))
box = pygame.image.load("images\Box.png")
box = pygame.transform.scale(box, (40, 50))
images = [paper_bag, box, pencil]

score = 0
font = pygame.font.SysFont("Arial", 30, bold=False, italic=True)
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

clock = pygame.time.Clock()
start_time = time.time()

run = True
while run: 
    clock.tick(60)
    timeElapsed = time.time()-start_time
    if timeElapsed > 30:
        if score > 20:
            screen.blit(green_earth, (0, 0))
            text = font.render("You did well", True, "black")
            screen.blit(text, (300, 250))
            pygame.display.update()
            time.sleep(5)
            break
        elif score < 20:
            screen.blit(green_earth, (0, 0))
            text = font.render("Better next time", True, "black")
            screen.blit(text, (300, 250))
            pygame.display.update()
            time.sleep(5)
            break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            bin.rect.center = pos
    screen.fill("sky blue")
    screen.blit(green_earth, (0, 0))
    score_text = font.render(str(score), True, (66, 38, 38))
    item_list = pygame.sprite.spritecollide(bin, Recycle_group, True)
    item_list2 = pygame.sprite.spritecollide(bin, Plastic_group, True)
    for item in item_list2:
        score -= 1
    for item in item_list:
        score += 1
    Bin_group.draw(screen)
    Plastic_group.draw(screen)
    screen.blit(score_text, (30, 20))
    Recycle_group.draw(screen)
    pygame.display.update()