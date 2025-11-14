import pygame
pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
stars = pygame.image.load("images\stars_2.png")
ship_yellow = pygame.image.load("images\Rocket_yellow.png")
ship_red = pygame.image.load("images\Rocket_red.png")
ship_yellow = pygame.transform.scale(ship_yellow, (60,60))
ship_red = pygame.transform.scale(ship_red, (60,60))
ship_red = pygame.transform.rotate(ship_red,(90))
ship_yellow = pygame.transform.rotate(ship_yellow,(270))
middel = pygame.Rect(400, 0, 10, 600)
class ship(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        if self.color == "yellow":
            self.image = ship_yellow
        elif self.color == "red":
            self.image = ship_red
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
    def movement(self, key):
        if self.color == "red":
            if key[pygame.K_a] and self.rect.x > -30:
                self.rect.x -= 3
            if key[pygame.K_d] and self.rect.x < 310:
                self.rect.x += 3
            if key[pygame.K_w] and self.rect.y < 0:
                self.rect.y -= 3
            if key[pygame.K_s] and self.rect.y > 600:
                self.rect.y += 3
        if self.color == "yellow":
            if key[pygame.K_LEFT]:
                self.rect.x -= 3
            if key[pygame.K_RIGHT]:
                self.rect.x += 3
            if key[pygame.K_UP]:
                self.rect.y -= 3
            if key[pygame.K_DOWN]:
                self.rect.y += 3
        
red_ship = ship(100, HEIGHT/2, "red")
yellow_ship = ship(700, HEIGHT/2, "yellow")
ship_group = pygame.sprite.Group()


run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(stars, (0,0))
    pygame.draw.rect(screen, "white", middel)
    screen.blit(red_ship.image, red_ship.rect.center)
    screen.blit(yellow_ship.image, yellow_ship.rect.center)
    key = pygame.key.get_pressed()
    red_ship.movement(key)
    yellow_ship.movement(key)
    pygame.display.update()