import pygame
import time
pygame.init()
WIDTH = 800
HEIGHT = 600
stars = pygame.image.load("images\stars.png")
rocket_img = pygame.image.load("images\space_ship.png")

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.x = x
        self.y = y
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
    def update(self, key):
        self.rect.y += 2
        if key[pygame.K_LEFT]:
            self.rect.x -= 2
        if key[pygame.K_RIGHT]:
            self.rect.x += 2
        if key[pygame.K_UP]:
            self.rect.y -= 3
        if key[pygame.K_DOWN]:
            self.rect.y += 2
        
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WIDTH - 150:
            self.rect.x = WIDTH - 150
        if self.rect.y < 0:
            self.rect.y = 0
       # if self.rect.y > HEIGHT - 219:
            #self.rect.y = HEIGHT - 219
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
rocket = Player(400,300, rocket_img)
rocket_group = pygame.sprite.Group()
rocket_group.add(rocket)
run = True
while run: 
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("sky blue")
    screen.blit(stars, (0,0))
    keys = pygame.key.get_pressed()
    rocket_group.update(keys)
    rocket_group.draw(screen)
    if rocket.rect.y > HEIGHT:
        run = False
    pygame.display.update() 
screen.blit(stars, (0,0))
font = pygame.font.SysFont("Times New Roman", 50, bold=True, italic=False)
text = font.render("GAME OVER", True, "WHITE")
screen.blit(text, (250, 150))
pygame.display.update()
time.sleep(2)
pygame.quit()
