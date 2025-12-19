import pygame
from random import randint, choice

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
white = pygame.image.load("images\white.jpeg")
white = pygame.transform.scale(white, (800, 600))
soldier_img = pygame.image.load("images\soldier.png")
soldier_img = pygame.transform.scale(soldier_img, (80, 100))
pirate_img = pygame.image.load("images\pirate.png")
pirate_img = pygame.transform.scale(pirate_img, (80, 100))
Red_Gem = pygame.image.load("images\Red_gem.png")
Red_Gem = pygame.transform.scale(Red_Gem, (40, 50))
White_Gem = pygame.image.load("images\white_gem.png")
White_Gem = pygame.transform.scale(White_Gem, (40, 50))
Blue_Gem = pygame.image.load("images\Blue_gem.png")
Blue_Gem = pygame.transform.scale(Blue_Gem, (40, 50))
images = [Red_Gem, Blue_Gem, White_Gem]
score = 0
font = pygame.font.SysFont("Arial", 30, bold=False, italic=True)
class Pirate(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pirate_img
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
class Gem(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = choice(images)
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
pirate = Pirate(350, 50)
Pirate_group = pygame.sprite.Group()
Pirate_group.add(pirate)
Gem_group = pygame.sprite.Group()
for i in range(30):
    gem = Gem(randint(20, 780), randint(20, 580))
    Gem_group.add(gem)

run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            pirate.rect.center = pos
    screen.fill("sky blue")
    screen.blit(white, (0, 0))
    score_text = font.render(str(score), True, (66, 38, 38))
    item_list = pygame.sprite.spritecollide(pirate, Gem_group, True)
    for item in item_list:
        score += 1
    Pirate_group.draw(screen)
    Gem_group.draw(screen)
    screen.blit(score_text, (50, 50))
    pygame.display.update()