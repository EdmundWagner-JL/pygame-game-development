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
red_health = 100
yellow_health = 100
font = pygame.font.SysFont("Calibri", 40, bold=True, italic=False)

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
        self.rect.topleft = self.x, self.y
    def movement(self, key):
        if self.color == "red":
            if key[pygame.K_a] and self.rect.left > -20:
                self.rect.x -= 1
            if key[pygame.K_d] and self.rect.right < 370:
                self.rect.x += 1
            if key[pygame.K_w] and self.rect.top > -20:
                self.rect.y -= 1
            if key[pygame.K_s] and self.rect.bottom < HEIGHT-30:
                self.rect.y += 1

        if self.color == "yellow":
            if key[pygame.K_LEFT] and self.rect.left > 380:
                self.rect.x -= 1
            if key[pygame.K_RIGHT] and self.rect.right < WIDTH - 30:
                self.rect.x += 1
            if key[pygame.K_UP] and self.rect.top > -20:
                self.rect.y -= 1
            if key[pygame.K_DOWN] and self.rect.bottom < HEIGHT - 30:
                self.rect.y += 1
    
class Bullet(pygame.sprite.Sprite):
    def __init__ (self,x,y,color):
        super().__init__()
        self.color = color
        self.x = x
        self.y= y
        self.rect = pygame.Rect(x, y, 10, 5)
    def update(self):
        if self.color == "yellow":
            self.rect.x -= 2
            if self.rect.x < 0:
                self.kill()
        if self.color == "red":
            self.rect.x += 2
            if self.rect.x > WIDTH:
                self.kill()

        
red_ship = ship(100, HEIGHT/2, "red")
yellow_ship = ship(700, HEIGHT/2, "yellow")
ship_group = pygame.sprite.Group()
Red_bullet = pygame.sprite.Group()
Yellow_bullet = pygame.sprite.Group()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RSHIFT:
                bullet = Bullet(yellow_ship.rect.x + 20, yellow_ship.rect.y + 60, "yellow")
                Yellow_bullet.add(bullet)
            if event.key == pygame.K_SPACE:
                bullet = Bullet(red_ship.rect.x + 70, red_ship.rect.y + 60, "red")
                Red_bullet.add(bullet)
    screen.blit(stars, (0,0))
    pygame.draw.rect(screen, "white", middel)
    screen.blit(red_ship.image, red_ship.rect.center)
    screen.blit(yellow_ship.image, yellow_ship.rect.center)
    for bullet in Yellow_bullet:
        pygame.draw.rect(screen,"yellow", bullet.rect)
    for bullet in Red_bullet:
        pygame.draw.rect(screen, "red", bullet.rect)
    for bullet in Yellow_bullet:
        if red_ship.rect.colliderect(bullet.rect):
            bullet.kill()
            red_health -= 10
    for bullet in Red_bullet:
        if yellow_ship.rect.colliderect(bullet.rect):
            bullet.kill()
            yellow_health -= 10
    
    red_health_text = font.render(str(red_health), True, "red")
    yellow_health_text = font.render(str(yellow_health), True, "yellow")
    screen.blit(red_health_text, (20, 20))
    screen.blit(yellow_health_text, (710, 20))
    
    key = pygame.key.get_pressed()
    red_ship.movement(key)
    yellow_ship.movement(key)
    Yellow_bullet.update()
    Red_bullet.update()
    if red_health <= 0 or yellow_health <= 0:
        if red_health <= 0:
            text = font.render("YELLOW WINS!", True, "yellow")
        else:
            text = font.render("RED WINS!", True, "red")

        screen.blit(text, (200, 250))
        pygame.display.update()
        pygame.time.delay(2000)
        run = False
    pygame.display.update()